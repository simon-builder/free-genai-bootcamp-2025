import { getWords } from "@/lib/api"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { BookOpen, Pencil, Sparkles, ArrowRight } from "lucide-react"
import Link from "next/link"

export default async function GroupsPage() {
  const words = await getWords()
  const verbCount = words.filter((word) => word.type === "verb").length
  const adjectiveCount = words.filter((word) => word.type === "adjective").length

  return (
    <div className="p-6">
      <div className="mb-8">
        <div className="flex items-center gap-2 mb-2">
          <Sparkles className="h-6 w-6 text-amber-500 dark:text-amber-400" />
          <span className="text-amber-600 dark:text-amber-400 text-sm font-medium">Word Categories</span>
        </div>
        <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100 mb-2">Learning Groups</h1>
        <p className="text-gray-600 dark:text-gray-400">Explore words by category to focus your learning</p>
        <div className="h-1 w-20 bg-gradient-to-r from-amber-500 to-orange-500 mt-4 rounded-full"></div>
      </div>

      <div className="grid md:grid-cols-2 gap-8">
        <Link href="/words?type=verb" className="block">
          <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm relative overflow-hidden h-full group">
            <div className="absolute inset-0 bg-gradient-to-br from-amber-50 to-orange-50 opacity-50 dark:hidden"></div>
            <CardHeader className="flex flex-row items-center space-x-4 pb-2 relative">
              <div className="p-3 bg-gradient-to-br from-amber-100 to-orange-100 dark:bg-gray-700 rounded-xl">
                <Pencil className="h-7 w-7 text-amber-700" />
              </div>
              <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Core Verbs</CardTitle>
            </CardHeader>
            <CardContent className="relative">
              <div className="space-y-4">
                <div>
                  <p className="text-5xl font-bold bg-gradient-to-r from-amber-600 to-orange-600 dark:text-amber-400 bg-clip-text text-transparent">
                    {verbCount}
                  </p>
                  <p className="text-gray-600 dark:text-gray-300 mt-2">Words in this category</p>
                </div>
                <div className="flex items-center text-amber-700 dark:text-amber-400 group-hover:text-amber-800 dark:group-hover:text-amber-300 transition-colors">
                  <span className="font-medium">View all verbs</span>
                  <ArrowRight className="h-5 w-5 ml-2 transform group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            </CardContent>
          </Card>
        </Link>

        <Link href="/words?type=adjective" className="block">
          <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm relative overflow-hidden h-full group">
            <div className="absolute inset-0 bg-gradient-to-br from-amber-50 to-orange-50 opacity-50 dark:hidden"></div>
            <CardHeader className="flex flex-row items-center space-x-4 pb-2 relative">
              <div className="p-3 bg-gradient-to-br from-amber-100 to-orange-100 dark:bg-gray-700 rounded-xl">
                <BookOpen className="h-7 w-7 text-amber-700" />
              </div>
              <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Core Adjectives</CardTitle>
            </CardHeader>
            <CardContent className="relative">
              <div className="space-y-4">
                <div>
                  <p className="text-5xl font-bold bg-gradient-to-r from-amber-600 to-orange-600 dark:text-amber-400 bg-clip-text text-transparent">
                    {adjectiveCount}
                  </p>
                  <p className="text-gray-600 dark:text-gray-300 mt-2">Words in this category</p>
                </div>
                <div className="flex items-center text-amber-700 dark:text-amber-400 group-hover:text-amber-800 dark:group-hover:text-amber-300 transition-colors">
                  <span className="font-medium">View all adjectives</span>
                  <ArrowRight className="h-5 w-5 ml-2 transform group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            </CardContent>
          </Card>
        </Link>
      </div>
    </div>
  )
}

