"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { getWords } from "@/lib/api"

export default function WordsTable({ initialWords }) {
  const [words, setWords] = useState(initialWords)
  const [currentPage, setCurrentPage] = useState(1)
  const [sortBy, setSortBy] = useState("kanji")
  const [order, setOrder] = useState("asc")
  const router = useRouter()

  const handleSort = async (column) => {
    const newOrder = sortBy === column && order === "asc" ? "desc" : "asc"
    setSortBy(column)
    setOrder(newOrder)
    const newWords = await getWords(currentPage, column, newOrder)
    setWords(newWords)
  }

  const handlePageChange = async (newPage) => {
    setCurrentPage(newPage)
    const newWords = await getWords(newPage, sortBy, order)
    setWords(newWords)
  }

  return (
    <>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead onClick={() => handleSort("kanji")}>Kanji</TableHead>
            <TableHead onClick={() => handleSort("romaji")}>Romaji</TableHead>
            <TableHead onClick={() => handleSort("english")}>English</TableHead>
            <TableHead onClick={() => handleSort("correct_count")}>Correct Count</TableHead>
            <TableHead onClick={() => handleSort("wrong_count")}>Wrong Count</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {words.map((word) => (
            <TableRow key={word.id}>
              <TableCell>{word.kanji}</TableCell>
              <TableCell>{word.romaji}</TableCell>
              <TableCell>{word.english}</TableCell>
              <TableCell>{word.correct_count}</TableCell>
              <TableCell>{word.wrong_count}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <div className="mt-4 flex justify-between">
        <Button onClick={() => handlePageChange(currentPage - 1)} disabled={currentPage === 1}>
          Previous
        </Button>
        <Button onClick={() => handlePageChange(currentPage + 1)}>Next</Button>
      </div>
    </>
  )
}

