import React from 'react'
import { useLocation, useHistory } from "react-router-dom";
import AlgoliaPlaces from 'algolia-places-react';
import axios from 'axios';

import { CoffeePic, 
        SignUpContainer, 
        IconContainer,
        ConfirmButton, 
        WinePic, 
        TitleText,
        SnackPic,
        ProductText,
        ProductContainer,
        TitleContainer, 
        PickFoodContainer
        } from './styled';

export const Signup = (props) => {
const location = useLocation();
const history = useHistory();
const [state, setState] = React.useState();
const [place, setPlace] = React.useState();

const onSubmit = () => {

    axios.post('https://23.239.24.16:5000/register_account', 
    { name: location?.state?.user['screen_name'], product: state, city: place})
        .then(data => console.info(data))
        .catch(err => console.info(err))

        history.push({
            pathname: '/home',
            state: { product: state,
            location: place
            }
          });
};


return (
    <SignUpContainer>
        <TitleContainer>
        <TitleText>{`Hello ${location?.state?.user?.screen_name}, \n Where are your located?`}</TitleText>
         <AlgoliaPlaces
      placeholder='Find your city'
 
      options={{
        appId: 'plJVZLK67SDJ',
        apiKey: '2ed8665cb0d2b8134545cf805e46b4f2',
      }}
 
      onChange={({ query, rawAnswer, suggestion, suggestionIndex }) => 
        setPlace(suggestion?.name)}
    />
        </TitleContainer>
            <PickFoodContainer>
            <TitleText>What do you sell?</TitleText>
        <IconContainer>
            <ProductContainer 
            pressed={state === 'wine' && true}
            onClick={() => setState('wine')}>
            <WinePic />
            <ProductText>Wine</ProductText>
            </ProductContainer>
            <ProductContainer 
            onClick={() => setState('snack')}
            pressed={state === 'snack' && true}
            >
            <SnackPic />
            <ProductText>Snacks</ProductText>
            </ProductContainer>
            <ProductContainer 
            onClick={() => setState('coffee')}
            pressed={state === 'coffee' && true}
            >
            <CoffeePic />
            <ProductText>Coffee</ProductText>
            </ProductContainer>   
            </IconContainer>  
            </PickFoodContainer>  
            <ConfirmButton onClick={onSubmit}>
                Confirm
            </ConfirmButton>
        </SignUpContainer>
    )
};