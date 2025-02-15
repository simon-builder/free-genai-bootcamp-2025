import { getWords, getWordsByGroup, getGroups } from "@/lib/api"
import WordsTable from "@/components/WordsTable"
import { Sparkles } from "lucide-react"

interface WordsPageProps {
  searchParams: { type?: 'verb' | 'adjective' }
}

export default async function WordsPage({ searchParams }: WordsPageProps) {
  try {
    // Get all groups first
    const groups = await getGroups()
    
    // Then find target group if type is specified
    const targetGroup = searchParams.type 
      ? groups.find(group => group.name === searchParams.type)
      : null

    if (searchParams.type && !targetGroup) {
      throw new Error(`Group not found for type: ${searchParams.type}`)
    }

    // Get words based on whether we have a group filter or not
    const words = targetGroup 
      ? await getWordsByGroup(targetGroup.id)
      : await getWords(1, "kanji", "asc")

    const pageTitle = searchParams.type 
      ? `${searchParams.type === 'verb' ? 'Verbs' : 'Adjectives'}`
      : 'All Words'
    
    const pageDescription = searchParams.type
      ? `Explore your ${searchParams.type === 'verb' ? 'verb' : 'adjective'} collection`
      : 'Explore and manage your Japanese vocabulary'

    return (
      <div className="p-6">
        <div className="mb-8">
          <div className="flex items-center gap-2 mb-2">
            <Sparkles className="h-6 w-6 text-amber-500" />
            <span className="text-amber-600 text-sm font-medium">
              {searchParams.type ? `${searchParams.type === 'verb' ? 'Verbs' : 'Adjectives'} Collection` : 'Word Collection'}
            </span>
          </div>
          <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100 mb-2">{pageTitle}</h1>
          <p className="text-gray-600 dark:text-gray-400">{pageDescription}</p>
          <div className="h-1 w-20 bg-gradient-to-r from-amber-500 to-orange-500 mt-4 rounded-full"></div>
        </div>

        <div className="bg-white/50 dark:bg-gray-800/50 rounded-xl shadow-sm border border-amber-100 dark:border-gray-800 backdrop-blur-sm">
          <WordsTable 
            initialWords={words} 
            wordType={searchParams.type}
            groupId={targetGroup?.id}
            allGroups={groups}
          />
        </div>
      </div>
    )
  } catch (error) {
    return (
      <div className="p-8 text-center">
        <div className="inline-block p-6 bg-orange-50 dark:bg-orange-900/20 text-orange-800 dark:text-orange-300 rounded-xl border border-orange-100 dark:border-orange-800/30 shadow-sm">
          <p className="font-medium">Error loading words</p>
          <p className="text-sm text-orange-600 dark:text-orange-400 mt-1">Please try again later</p>
        </div>
      </div>
    )
  }
}