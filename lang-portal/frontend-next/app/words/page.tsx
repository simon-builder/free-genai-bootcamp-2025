import { getWords } from "@/lib/api"
import WordsTable from "@/components/WordsTable"
// import AddWordForm from "@/components/AddWordForm"

export default async function WordsPage() {
  const words = await getWords()

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Words</h1>
        <AddWordForm />
      </div>
      <WordsTable initialWords={words} />
    </div>
  )
}

