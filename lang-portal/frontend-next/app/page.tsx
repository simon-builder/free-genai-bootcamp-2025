import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { ArrowRight, BookOpen, Layers, Activity, Sparkles } from "lucide-react"
import { getWords } from "@/lib/api"
import Link from "next/link"

export default async function Dashboard() {
  const words = await getWords()
  const verbCount = words.filter(word => word.type === "verb").length
  const adjectiveCount = words.filter(word => word.type === "adjective").length

  return (
    <div className="p-6 from-amber-50/50 to-transparent min-h-screen">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-12">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <Sparkles className="h-6 w-6 text-amber-500" />
            <span className="text-amber-600 text-sm font-medium">Welcome Back!</span>
          </div>
          <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100">Your Learning Space</h1>
          <p className="text-gray-600 dark:text-gray-100 mt-2">Continue your Japanese language journey</p>
          <div className="h-1 w-20 bg-gradient-to-r from-amber-500 to-orange-500 mt-4 rounded-full"></div>
        </div>
        <Link href="/study">
          <Button className="mt-6 md:mt-0 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white px-8 py-6 rounded-xl flex items-center gap-3 shadow-lg hover:shadow-xl transition-all text-lg">
            <Activity className="h-6 w-6" />
            Start Learning
            <ArrowRight className="h-6 w-6" />
          </Button>
        </Link>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm">
          <CardHeader className="flex flex-row items-center space-x-4 pb-2">
            <div className="p-3 bg-gradient-to-br from-amber-100 to-orange-100 rounded-xl">
              <BookOpen className="h-7 w-7 text-amber-700" />
            </div>
            <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Vocabulary Progress</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-5xl font-bold bg-gradient-to-r from-amber-600 to-orange-600 bg-clip-text text-transparent dark:text-amber-400">
              {words.length}
            </p>
            <p className="text-gray-600 dark:text-gray-300 mt-2">Words in your collection</p>
          </CardContent>
        </Card>

        <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm">
          <CardHeader className="flex flex-row items-center space-x-4 pb-2">
            <div className="p-3 bg-gradient-to-br from-orange-100 to-amber-100 rounded-xl">
              <Layers className="h-7 w-7 text-orange-700" />
            </div>
            <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Word Categories</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <p className="text-3xl font-bold text-orange-600 dark:text-amber-400">{verbCount}</p>
                <p className="text-gray-600 dark:text-gray-300">Core Verbs</p>
              </div>
              <div>
                <p className="text-3xl font-bold text-orange-600 dark:text-amber-400">{adjectiveCount}</p>
                <p className="text-gray-600 dark:text-gray-300">Core Adjectives</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-amber-50 to-orange-50 opacity-50 dark:hidden"></div>
          <CardHeader className="flex flex-row items-center space-x-4 pb-2 relative">
            <div className="p-3 bg-gradient-to-br from-amber-100 to-orange-100 dark:bg-gray-700 rounded-xl">
              <Activity className="h-7 w-7 text-amber-700" />
            </div>
            <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Study Sessions</CardTitle>
          </CardHeader>
          <CardContent className="relative">
            <p className="text-3xl font-bold text-amber-700 dark:text-amber-400">Coming Soon</p>
            <p className="text-gray-600 dark:text-gray-300 mt-2">Track your learning progress</p>
            <div className="mt-4">
              <Button 
                variant="outline" 
                className="text-amber-700 dark:text-amber-400 border-amber-200 dark:border-gray-600" 
                disabled
              >
                View Stats
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

