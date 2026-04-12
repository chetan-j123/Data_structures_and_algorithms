var canConstruct = function(ransomNote, magazine) {
  let ransom_note_chars={};
  for(let i=0;i<ransomNote.length;i++){
    ransom_note_chars[ransomNote[i]]=  (ransom_note_chars[ransomNote[i]]||0)+1
  }
  for (let i=0;i<magazine.length;i++){
    if(magazine[i] in ransom_note_chars){
       ransom_note_chars[magazine[i]]=ransom_note_chars[magazine[i]]-1
       if (ransom_note_chars[magazine[i]]==0){
         delete ransom_note_chars[magazine[i]]
      }
    }
    if (Object.keys(ransom_note_chars).length==0){
      return true
    }
  }
  return false
};
