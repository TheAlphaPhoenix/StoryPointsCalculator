// Backend Velo (Wix) Code for Story Points Calculator - Enhanced UI Version

// Function to calculate story points based on user input
export function calculateStoryPoints(scope, stakeholders, compliance, dataAnalysis, operations, timeCommitment, risk) {
    const scores = {
        "Low": 1,
        "Medium": 3,
        "High": 5
    };
    
    // Calculate total score based on inputs
    let totalScore = scores[scope] + scores[stakeholders] + scores[compliance] + 
                     scores[dataAnalysis] + scores[operations] + scores[timeCommitment] + scores[risk];
    
    // Map total score to Fibonacci-based story points
    let storyPoints;
    if (totalScore <= 8) {
        storyPoints = 1;
    } else if (totalScore <= 12) {
        storyPoints = 2;
    } else if (totalScore <= 16) {
        storyPoints = 3;
    } else if (totalScore <= 22) {
        storyPoints = 5;
    } else if (totalScore <= 28) {
        storyPoints = 8;
    } else if (totalScore <= 34) {
        storyPoints = 13;
    } else {
        storyPoints = 21;
    }
    
    return {
        totalScore: totalScore,
        storyPoints: storyPoints,
        complexityLevel: storyPoints <= 3 ? "Simple" : storyPoints <= 8 ? "Moderate" : "Complex",
        suggestedSprint: storyPoints <= 5 ? "Short-Term" : storyPoints <= 13 ? "Mid-Term" : "Long-Term"
    };
}

// Frontend Code - Enhanced UI Styling
$w.onReady(function () {
    $w("#calculateButton").onClick(() => {
        let scope = $w("#dropdownScope").value;
        let stakeholders = $w("#dropdownStakeholders").value;
        let compliance = $w("#dropdownCompliance").value;
        let dataAnalysis = $w("#dropdownDataAnalysis").value;
        let operations = $w("#dropdownOperations").value;
        let timeCommitment = $w("#dropdownTimeCommitment").value;
        let risk = $w("#dropdownRisk").value;

        let result = calculateStoryPoints(scope, stakeholders, compliance, dataAnalysis, operations, timeCommitment, risk);
        
        // Apply Modern UI Enhancements
        $w("#textTotalScore").text = `Total Score: ${result.totalScore}`;
        $w("#textTotalScore").style.color = "#00A8E8";
        $w("#textTotalScore").style.fontSize = "18px";

        $w("#textStoryPoints").text = `Story Points: ${result.storyPoints}`;
        $w("#textStoryPoints").style.color = "#FF5733";
        $w("#textStoryPoints").style.fontSize = "20px";
        $w("#textStoryPoints").style.fontWeight = "bold";
        
        $w("#textComplexity").text = `Complexity Level: ${result.complexityLevel}`;
        $w("#textComplexity").style.color = "#2ECC71";

        $w("#textSprint").text = `Suggested Sprint Length: ${result.suggestedSprint}`;
        $w("#textSprint").style.color = "#F39C12";
    });
});
