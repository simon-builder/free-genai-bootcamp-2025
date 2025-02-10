import { getWords } from "@/lib/api"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { BookOpen, Pencil } from "lucide-react"

export default async function GroupsPage() {
  const words = await getWords()
  
  const verbCount = words.filter((word) => word.type === "verb").length
  const adjectiveCount = words.filter((word) => word.type === "adjective").length

  return (
    <div className="container mx-auto py-8 px-4">
      <h1 className="text-3xl font-bold mb-8 text-gray-800">Word Categories</h1>
      <div className="grid md:grid-cols-2 gap-6">
        <Card className="hover:shadow-lg transition-shadow">
          <CardHeader className="flex flex-row items-center space-x-4 pb-2">
            <div className="p-2 bg-blue-100 rounded-lg">
              <Pencil className="h-6 w-6 text-blue-700" />
            </div>
            <CardTitle>Core Verbs</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="mt-2 space-y-2">
              <p className="text-2xl font-bold text-blue-700">{verbCount}</p>
              <p className="text-sm text-gray-500">Total words in this category</p>
              <a 
                href="/words?type=verb" 
                className="inline-block mt-4 text-blue-600 hover:text-blue-800 text-sm font-medium"
              >
                View all verbs →
              </a>
            </div>
          </CardContent>
        </Card>

        <Card className="hover:shadow-lg transition-shadow">
          <CardHeader className="flex flex-row items-center space-x-4 pb-2">
            <div className="p-2 bg-purple-100 rounded-lg">
              <BookOpen className="h-6 w-6 text-purple-700" />
            </div>
            <CardTitle>Core Adjectives</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="mt-2 space-y-2">
              <p className="text-2xl font-bold text-purple-700">{adjectiveCount}</p>
              <p className="text-sm text-gray-500">Total words in this category</p>
              <a 
                href="/words?type=adjective" 
                className="inline-block mt-4 text-purple-600 hover:text-purple-800 text-sm font-medium"
              >
                View all adjectives →
              </a>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

