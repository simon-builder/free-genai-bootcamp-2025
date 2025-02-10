import { getWords } from "@/lib/api"
import WordsTable from "@/components/WordsTable"
import AddWordForm from "@/components/AddWordForm"
import { Button } from "@/components/ui/button"
import { Plus } from "lucide-react"

export default async function WordsPage() {
  try {
    const initialWords = await getWords(1, "kanji", "asc")
    
    return (
      <div className="container mx-auto py-8 px-4">
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-800">Words</h1>
            <p className="text-gray-500 mt-1">Manage your Japanese vocabulary</p>
          </div>
          <Button className="flex items-center gap-2">
            <Plus className="h-4 w-4" />
            Add Word
          </Button>
        </div>
        <WordsTable initialWords={initialWords} />
      </div>
    )
  } catch (error) {
    return (
      <div className="p-8 text-center">
        <div className="inline-block p-4 bg-red-50 text-red-700 rounded-lg">
          Error loading words. Please try again later.
        </div>
      </div>
    )
  }
}

