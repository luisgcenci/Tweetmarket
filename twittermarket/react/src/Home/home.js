import React from 'react'
import axios from 'axios';
import { useLocation } from "react-router-dom";


import {HomeContainer, ContentFeed, Post, Username, UserLocation, UserTag, Tweet, UserText, TextContainer, ItemsContainer, UserPos, UserDate} from './styled';
import { CoffeePic, SnackPic, WinePic } from '../Signup/styled';

export const Home = () => {
    const location = useLocation();
    const [state, setState] = React.useState();

    React.useEffect(() => {
        axios.post('https://23.239.24.16:5000/get_requests', {product: location?.state?.product, city: location?.state?.location })
        .then(data => {console.log(data)
        setState(data.data.reverse())        
        })
        .catch(err => console.log(err))
    }, [location?.state?.location, location?.state?.product]);
    console.log(state);
    return (
    <HomeContainer>
        <ContentFeed>
            {state?.map(item => {
              return ( 
                    <Post key={item[5]}>
                    <ItemsContainer>
                       {state[0][3] === 'wine' && <WinePic />}
                       {state[0][3] === 'snacks' && <SnackPic />}
                       {state[0][3] === 'coffee' && <CoffeePic />}
                       <TextContainer>
                           <UserPos>
                       <UserText>
                        <Username>{item[0]}</Username>
                        {item[1] && <UserTag>@{item[1]}</UserTag>}
                       </UserText>
              <UserLocation>{item[4]}</UserLocation>
                           </UserPos>
                    <Tweet>{item[2]}</Tweet>
              <UserDate>{item[5]}</UserDate>
                       </TextContainer>
                    </ItemsContainer>
                </Post>
              )
            })}
        </ContentFeed>
    </HomeContainer>      
    )
};