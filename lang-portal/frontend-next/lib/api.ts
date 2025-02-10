import axios from "axios"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000"

const api = axios.create({
  baseURL: API_BASE_URL,
})

export const getWords = async (page = 1, sortBy = "kanji", order = "asc") => {
  const response = await api.get(`/words?page=${page}&sort_by=${sortBy}&order=${order}`)
  return response.data
}

export const getWord = async (id: number) => {
  const response = await api.get(`/words/${id}`)
  return response.data
}

export const createWord = async (wordData: any) => {
  const response = await api.post("/words", wordData)
  return response.data
}

export const getGroups = async (page = 1) => {
  const response = await api.get(`/groups?page=${page}`)
  return response.data
}

export const getGroup = async (id: number) => {
  const response = await api.get(`/groups/${id}`)
  return response.data
}

export const createGroup = async (groupData: any) => {
  const response = await api.post("/groups", groupData)
  return response.data
}

export const addWordToGroup = async (groupId: number, wordId: number) => {
  const response = await api.post(`/groups/${groupId}/words/${wordId}`)
  return response.data
}

export const createStudySession = async () => {
  const response = await api.post("/study_sessions")
  return response.data
}

export const logWordReview = async (sessionId: number, reviewData: any) => {
  const response = await api.post(`/study_sessions/${sessionId}/review`, reviewData)
  return response.data
}

