import axios from "axios"

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000"
})

export interface Word {
  id: number
  kanji: string
  romaji: string
  english: string
  parts: any // TODO: Define proper type for parts
  type: string
  correct_count: number
  wrong_count: number
}

export interface WordCreate {
  kanji: string
  romaji: string
  english: string
  parts: any
  type: "verb" | "adjective"
}

export interface Group {
  id: number
  name: string
  description: string
}

// Words API
export const getWords = async (page?: number, sortBy = "kanji", order: "asc" | "desc" = "asc") => {
  const params = new URLSearchParams()
  if (page) params.append("page", page.toString())
  params.append("sort_by", sortBy)
  params.append("order", order)

  const response = await api.get<Word[]>(`/words?${params}`)
  return response.data
}

export const getWord = async (id: number) => {
  const response = await api.get<Word>(`/words/${id}`)
  return response.data
}

export const createWord = async (word: WordCreate) => {
  const response = await api.post<Word>("/words", word)
  return response.data
}

// Study Sessions API
export const createStudySession = async () => {
  const response = await api.post("/study_sessions")
  return response.data
}

export const logWordReview = async (sessionId: number, reviewData: any) => {
  const response = await api.post(`/study_sessions/${sessionId}/review`, reviewData)
  return response.data
}

