import { useNavigate } from "react-router-dom";

function Upload() {
  const navigate = useNavigate();

  const uploadImage = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("image", file);

    const res = await fetch("http://127.0.0.1:5000/api/predict", {
      method: "POST",
      headers: {
        Authorization: localStorage.getItem("token"),
      },
      body: formData,
    });

    const data = await res.json();
    localStorage.setItem("result", JSON.stringify(data));
    navigate("/result");
  };

  return (
    <div>
      <h2>Upload Skin Image</h2>
      <input type="file" onChange={uploadImage} />
      <button onClick={() => { localStorage.clear(); navigate("/"); }}>
        Logout
      </button>
    </div>
  );
}

export default Upload;