import { useQuery } from "@tanstack/react-query";

const Home = () => {
  const getToken = async () => {
    const response = await fetch("http://127.0.0.1:8000/token");

    const token = await response.json();

    return token;
  };

  const getGames = async () => {
    const response = await fetch("http://127.0.0.1:8000/games");

    const games = await response.json();

    return games;
  };

  const { data: tokenData } = useQuery({
    queryKey: ["token"],
    queryFn: () => getToken(),
  });

  const { data: gameData } = useQuery({
    queryKey: ["game"],
    queryFn: () => getGames(),
  });

  console.log(gameData);
  return <h1>Hello</h1>;
};

export default Home;
