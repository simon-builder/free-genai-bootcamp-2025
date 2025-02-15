import axios from "axios"

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000"
})

export interface Word {
  id: number
  kanji: string
  romaji: string
  english: string
  parts: Array<{ kanji: string; romaji: string[] }>
  groups: Array<{ id: number; name: string }>
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
export const getWords = async (
  page: number = 1,
  orderBy: string = "kanji",
  order: "asc" | "desc" = "asc"
): Promise<Word[]> => {
  const response = await api.get<Word[]>(`/words?page=${page}&order_by=${orderBy}&order=${order}`)
  console.log('Words API Response:', JSON.stringify(response.data, null, 2))
  return response.data
}

export const getWordsByGroup = async (
  groupId: number,
  page: number = 1,
  orderBy: string = "kanji",
  order: "asc" | "desc" = "asc"
): Promise<Word[]> => {
  const response = await api.get<{ words: Word[] }>(`/groups/${groupId}?page=${page}&order_by=${orderBy}&order=${order}`)
  return response.data.words
}

export const getGroups = async (
  page: number = 1
): Promise<Group[]> => {
  const response = await api.get<Group[]>(`/groups?page=${page}`)
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

export const getAllWords = async (): Promise<Word[]> => {
  const response = await api.get<Word[]>(`/words?limit=0`)  // limit=0 means no limit
  return response.data
}

