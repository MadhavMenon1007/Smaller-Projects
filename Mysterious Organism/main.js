// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G'];
  return dnaBases[Math.floor(Math.random() * 4)];
};

// Returns a random single strand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = [];
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase());
  }
  return newStrand;
};

// Creates a pAqeour object
const pAqeourFactory=(num, dnaBases)=>{
  return {
    specimenNum:num,
    dnaBase:dnaBases,
    mutate(){  // Randomly changes one DNA base
      const randomIndex=Math.floor(Math.random()*this.dnaBase.length+1);
      let chosenBase=this.dnaBase[randomIndex];
      switch (chosenBase){
        case "A":
          this.dnaBase[randomIndex]=["T", "C", "G"][Math.floor(Math.random()*["T", "C", "G"].length)];
          break;
        case "T":
          this.dnaBase[randomIndex]=["A", "C", "G"][Math.floor(Math.random()*["A", "C", "G"].length)];
          break;
        case "C":
          this.dnaBase[randomIndex]=["A", "T", "G"][Math.floor(Math.random()*["A", "T", "G"].length)];
          break;
        case "G":
          this.dnaBase[randomIndex]=["A", "T", "C"][Math.floor(Math.random()*["A", "T", "C"].length)];
          break;
  
      }
      return this.dnaBase;
    },

    compareDNA(pAqeourOrganism){ // Compares two organisms and returns a percentage based on how many DNA bases they share at the same index
      let count=0;
      for (let i=0;i<this.dnaBase.length;i++){
        if (this.dnaBase[i]===pAqeourOrganism.dnaBase[i]){
          count+=1;
        }
      }
      const countPercentage = (count/this.dnaBase.length)*100;
      console.log(`Specimen ${this.specimenNum} and Specimen ${obj.specimenNum} have ${countPercentage}% DNA in common`);
    },
    willLikelySurvive(){ // Organism can only survive if their bases are comprised of 60% C and G
      let count=0;
      for (const base of this.dnaBase){
        if (base==="C"||base==="G"){
          count+=1;
        }
      }
      const countPercentage=(count/this.dnaBase.length)*100;
      return (countPercentage>=60?true:false);
    },

    complementStrand(){ // Switches their strand to its complement
      let compStrand=[];
      for (let i=0;i<this.dnaBase.length;i++){
        switch (this.dnaBase[i]){
          case "A":
            compStrand.push("T");
            break;
          case "T":
            compStrand.push("A");
            break;
          case "C":
            compStrand.push("G");
            break;
          case "G":
            compStrand.push("C");
            break;
          default:
            return "Invalid base";
        }
      }
      return compStrand;
    }
  }

 
};

const createThirtySpecimenThatCanSurvive=()=>{ // Creates thirty organisms that will survive
  const specimenArray=[];
  for (let i=0;i<=1000000000;i++){
    if ((pAqeourFactory(i, mockUpStrand())).willLikelySurvive()){
      specimenArray.push(pAqeourFactory(i, mockUpStrand()));
    }

    if (specimenArray.length===30){
      break;
    }
  }
  return specimenArray;
}


