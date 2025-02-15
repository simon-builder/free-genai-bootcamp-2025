"use client"

import { useState } from "react"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { getWords, getWordsByGroup, type Word, type Group } from "@/lib/api"
import { ChevronLeft, ChevronRight } from "lucide-react"

interface WordsTableProps {
  initialWords: Word[]
  wordType?: 'verb' | 'adjective'
  groupId?: number
  allGroups: Group[]
}

export default function WordsTable({ initialWords, wordType, groupId, allGroups }: WordsTableProps) {
  const [words, setWords] = useState(initialWords)
  const [currentPage, setCurrentPage] = useState(1)
  const [isLoading, setIsLoading] = useState(false)

  const handlePageChange = async (newPage: number) => {
    if (newPage < 1) return
    setIsLoading(true)
    try {
      let newWords: Word[] = []
      if (groupId) {
        newWords = await getWordsByGroup(groupId, newPage)
      } else {
        newWords = await getWords(newPage)
      }
      setWords(newWords)
      setCurrentPage(newPage)
    } catch (error) {
      console.error('Error changing page:', error)
    } finally {
      setIsLoading(false)
    }
  }

  const getWordGroup = (word: Word) => {
    // Find the word's group ID from its groups array
    const wordGroupId = word.groups?.[0]?.id
    if (!wordGroupId) return null
    
    // Find the matching group from allGroups
    return allGroups.find(g => g.id === wordGroupId)
  }

  return (
    <div className="space-y-4">
      <div className="overflow-hidden">
        <Table>
          <TableHeader>
            <TableRow className="bg-amber-50/50 dark:bg-gray-800">
              <TableHead className="font-medium text-amber-900 dark:text-gray-200">Kanji</TableHead>
              <TableHead className="font-medium text-amber-900 dark:text-gray-200">Romaji</TableHead>
              <TableHead className="font-medium text-amber-900 dark:text-gray-200">English</TableHead>
              {!wordType && (
                <TableHead className="font-medium text-amber-900 dark:text-gray-200">Type</TableHead>
              )}
            </TableRow>
          </TableHeader>
          <TableBody>
            {words.map((word) => {
              const group = getWordGroup(word)
              return (
                <TableRow 
                  key={word.id}
                  className="hover:bg-amber-50/30 dark:hover:bg-gray-700/50 transition-colors duration-200"
                >
                  <TableCell className="font-medium text-gray-900 dark:text-gray-100">{word.kanji}</TableCell>
                  <TableCell className="text-gray-700 dark:text-gray-300">{word.romaji}</TableCell>
                  <TableCell className="text-gray-700 dark:text-gray-300">{word.english}</TableCell>
                  {!wordType && (
                    <TableCell>
                      <span className={`px-3 py-1 rounded-full text-xs font-medium ${
                        group?.name === 'verb'
                          ? 'bg-green-200 text-amber-800 dark:bg-green-900 dark:text-green-100' 
                          : 'bg-orange-200 text-orange-800 dark:bg-orange-900 dark:text-orange-100'
                      }`}>
                        {group?.name || 'unknown'}
                      </span>
                    </TableCell>
                  )}
                </TableRow>
              )
            })}
          </TableBody>
        </Table>
      </div>

      <div className="flex justify-between items-center px-4 py-2">
        <Button
          variant="ghost"
          size="sm"
          onClick={() => handlePageChange(currentPage - 1)}
          disabled={currentPage === 1 || isLoading}
          className="text-amber-800 hover:text-amber-900 hover:bg-amber-100 dark:text-gray-300 dark:hover:text-gray-100 dark:hover:bg-gray-700 flex items-center gap-2"
        >
          <ChevronLeft className="h-4 w-4" />
          Previous
        </Button>
        <span className="text-sm text-amber-800 dark:text-gray-300">Page {currentPage}</span>
        <Button
          variant="ghost"
          size="sm"
          onClick={() => handlePageChange(currentPage + 1)}
          disabled={isLoading}
          className="text-amber-800 hover:text-amber-900 hover:bg-amber-100 dark:text-gray-300 dark:hover:text-gray-100 dark:hover:bg-gray-700 flex items-center gap-2"
        >
          Next
          <ChevronRight className="h-4 w-4" />
        </Button>
      </div>
    </div>
  )
}