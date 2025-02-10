"use client"

import { useState } from "react"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { getWords, type Word } from "@/lib/api"
import { ChevronLeft, ChevronRight } from "lucide-react"

export default function WordsTable({ initialWords }: { initialWords: Word[] }) {
  const [words, setWords] = useState(initialWords)
  const [currentPage, setCurrentPage] = useState(1)
  const [isLoading, setIsLoading] = useState(false)

  const handlePageChange = async (newPage: number) => {
    if (newPage < 1) return
    setIsLoading(true)
    try {
      const newWords = await getWords(newPage)
      setWords(newWords)
      setCurrentPage(newPage)
    } catch (error) {
      console.error('Error changing page:', error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="space-y-4">
      <div className="border rounded-lg overflow-hidden">
        <Table>
          <TableHeader>
            <TableRow className="bg-gray-50">
              <TableHead className="font-semibold">Kanji</TableHead>
              <TableHead className="font-semibold">Romaji</TableHead>
              <TableHead className="font-semibold">English</TableHead>
              <TableHead className="font-semibold">Type</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {words.map((word) => (
              <TableRow 
                key={word.id}
                className="hover:bg-gray-50 transition-colors"
              >
                <TableCell className="font-medium">{word.kanji}</TableCell>
                <TableCell>{word.romaji}</TableCell>
                <TableCell>{word.english}</TableCell>
                <TableCell>
                  <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                    word.type === 'verb' 
                      ? 'bg-blue-100 text-blue-700' 
                      : 'bg-purple-100 text-purple-700'
                  }`}>
                    {word.type}
                  </span>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>

      <div className="flex justify-between items-center px-4">
        <Button
          variant="outline"
          size="sm"
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1 || isLoading}
          className="flex items-center gap-2"
        >
          <ChevronLeft className="h-4 w-4" />
          Previous
        </Button>
        <span className="text-sm text-gray-500">Page {currentPage}</span>
        <Button
          variant="outline"
          size="sm"
          onClick={() => handlePageChange(currentPage + 1)}
          disabled={isLoading}
          className="flex items-center gap-2"
        >
          Next
          <ChevronRight className="h-4 w-4" />
        </Button>
      </div>
    </div>
  )
}

