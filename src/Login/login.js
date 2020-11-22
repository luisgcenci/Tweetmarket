import React from 'react'
import TwitterLogin from "react-twitter-login";
import { useHistory } from "react-router-dom";
import { ButtonContainer, LoginContainer, TitleText } from './styled';

export const Login = () => {
  const history = useHistory();
  const authHandler = async (err, data) => {
    console.log(data)
    await data
    if (data?.screen_name){
      history.push({
        pathname: '/signup',
        state: { user: data }
      });
    }
  };

  return (
    <LoginContainer>
      <ButtonContainer>
        <TitleText>
          Welcome to Tweetmarket!
        </TitleText>
      <TwitterLogin
      authCallback={authHandler}
      consumerKey={'6mLNLbYRSnM0OQpQESvkwbFiQ'}
      consumerSecret={'7YqSQck3Gg3pEywfsGcz6BGAGWcrazlEixYaAc8gkoetAReqHR'}
    />
      </ButtonContainer>
    </LoginContainer>
  );
};