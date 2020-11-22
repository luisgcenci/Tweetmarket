import styled, {css} from 'styled-components';
import { ReactComponent as WineIcon} from '../assets/red.svg';
import { ReactComponent as SnackIcon} from '../assets/snack.svg';
import { ReactComponent as CoffeeIcon} from '../assets/coffee-cup.svg';

export const SignUpContainer = styled.div`
display: flex;
flex-direction: column;
justify-content: space-around;
align-items: center;
width: 100%;
height: 100vh;
`;

export const IconContainer = styled.div`
    display: flex;
    width: 60%;
    height: 30;
    align-items: center;
    justify-content: space-between;
    margin-top: 24px;
`;

export const PickFoodContainer = styled.div`
    display: flex;
    width: 100%;
    flex-direction: column;
    align-items: center;
    justify-content: center;
`;

export const TitleContainer = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 20%;
    align-items: center;
    justify-content: center;
`;

export const WinePic = styled(WineIcon)`
    height: 64px;
    width: 64px;
`;

export const SnackPic = styled(SnackIcon)`
    height: 64px;
    width: 64px;
`;

export const CoffeePic = styled(CoffeeIcon)`
    height: 64px;
    width: 64px;
`;

export const TitleText = styled.h2`
    color: #1DA1F2;
    font-size: 2em;
    white-space: pre-line;
`;

export const ProductText = styled.p`
color: #14171A;
font-size: 1em;
font-weight: bold;
font-family: "Roboto", "Helvetica", "Arial", sans-serif;
`;

export const ProductContainer = styled.div`
display: flex;
align-items: center;
justify-content: center;
flex-direction: column;
border: solid;
border-width: 1px;
border-radius: 10px;
padding: 24px;
border-color: #1DA1F2;
box-shadow: 3px 3px #1DA1F2;
${({ pressed }) => pressed && css`
    background-color: #1DA1F2;
    box-shadow: 3px 3px #FFFFFF;
    ${ProductText} {
        color: #FFFFFF;
    }
    `};
`;

export const ConfirmButton = styled.button`
    color: #fff;
    background-color: rgb(29, 161, 242);
    align-items: center;
    user-select: none;
    border-radius: 10px;
    vertical-align: middle;
    justify-content: center;
    min-width: 64px;
    border-color: transparent;
    transition: background-color 250ms,
    cubic-bezier(0.4, 0, 0.2, 1) 0ms,
    box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,
    border 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
    font-family: "Roboto", "Helvetica", "Arial", sans-serif;
    font-size: 1.5rem;
    cursor: pointer;
    display: inline-flex;
    outline: none;
    padding: 1em;
    font-weight: bold;
    &:hover {
        background-color: "rgb(29, 145, 218)";
       }
`;