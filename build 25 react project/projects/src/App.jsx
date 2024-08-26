import './App.css'
import Accoridian from './component/accordian';
import RandomColor from './component/random-color';
import StarRating from './component/star-rating';
function App() {

  return (
    <div className="App">
      {/* <Accoridian/>
      <RandomColor/> */}
      {/* <StarRating/> */}
      <ImageSlider
        url={"https://picsum.photos/v2/list"}
        page={"1"}
        limit={"10"}
      />
    </div>
  );
}

export default App
