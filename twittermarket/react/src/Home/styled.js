import styled from 'styled-components';

export const HomeContainer = styled.div`
display: flex;
justify-content: center;
width: 100%;
`;

export const ContentFeed = styled.div`
background-color: white;
width: 50%;
height: 100%;
`;

export const Post = styled.div`
width: 100%;
min-height: 100px;
align-items: center;
justify-content: center;
padding: 28px 0px;
`;

export const Username = styled.p`
    font-size: 1em;
    font-weight: bold;
    font-family: "Roboto", "Helvetica", "Arial", sans-serif;
    color: #14171A;
`;

export const UserTag = styled.p`
    font-size: 0.9em;
    font-weight: normal;
    font-family: "Roboto", "Helvetica", "Arial", sans-serif;
    color: #AAB8C2;
    margin-left: 8px;
`;

export const Tweet = styled.p`
    font-size: 1em;
    font-family: "Roboto", "Helvetica", "Arial", sans-serif;
    color: #14171A;
    flex-wrap: wrap;
`;


export const ItemsContainer = styled.div`
display: flex;
flex-direction: row;
justify-content: flex-start;
align-items: center;
border: solid;
border-width: 1px;
border-radius: 10px;
border-color: #1DA1F2;
box-shadow: 3px 3px #1DA1F2;
padding: 24px 0;
`;

export const TextContainer = styled.div`
    display: flex;
    flex-direction: column;
    margin-left: 16px;
    align-items: flex-start;
`;

export const UserText = styled.div` 
display: flex;
flex-direction: row;
align-items: center;
`;

export const UserPos = styled.div`
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: space-between;
`;

export const UserLocation = styled.p` 
 font-size: 0.7em;
    font-weight: bold;
    font-family: "Roboto", "Helvetica", "Arial", sans-serif;
    color: #AAB8C2;
    margin-left: 8px;
`;

export const UserDate = styled.p` 
font-size: 0.7em;
   font-weight: bold;
   font-family: "Roboto", "Helvetica", "Arial", sans-serif;
   color: #AAB8C2;
`;
