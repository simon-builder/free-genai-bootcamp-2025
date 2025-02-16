# Writing Practice App

Due to limited information in the assignment document,
https://docs.google.com/document/d/1KVDTDF4t8VtI69F5KMo67KoTBXgVhsd2O9hK-uPh2rA/edit?tab=t.lrj6eqolqwwv

the following assumptions have been made for this implementation.

## Goal
Enable users to practice writing simple sentences and receive feedback through image recognition.

## Acceptance Criteria
- [ ] Users can select word groups (verbs, adjectives, etc.) to practice with
- [ ] Users receive simple English sentences to translate
- [ ] Users can upload photos of their handwritten Japanese answers
- [ ] System accurately recognizes and verifies Japanese handwriting
- [ ] Users receive clear feedback on their writing accuracy
- [ ] Practice sessions cover words from their selected word groups

## Constraints
- Limited to Japanese language only (due to MangaOCR)
- Sentences will be basic structure only (Subject + Object + Verb)
- Vocabulary limited to words available in lang-portal database
- OCR accuracy dependent on handwriting clarity and image quality

## Additional Information
- Integrates with lang-portal's word database
- Focus on common daily expressions for practical learning (N5 to N3 level)

## Personal Learning Goals
- Gain hands-on experience with MangaOCR (and its limitations)
- Understand integration between standalone tools and main applications
- Bonus: Use a popular IIT model for OCR instead of MangaOCR