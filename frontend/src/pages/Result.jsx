function Result() {
  const data = JSON.parse(localStorage.getItem("result"));

  if (!data) return <h2>No Result</h2>;

  return (
    <div>
      <h2>Prediction Result</h2>
      <p><b>Disease:</b> {data.predicted_disease}</p>
      <p><b>Confidence:</b> {data.confidence}%</p>

      <h3>Description</h3>
      <p>{data.assistance.description}</p>

      <h3>Care Tips</h3>
      <ul>
        {data.assistance.care_tips.map((tip, i) => <li key={i}>{tip}</li>)}
      </ul>
    </div>
  );
}

export default Result;