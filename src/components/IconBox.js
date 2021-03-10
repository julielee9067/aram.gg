import { Image } from '@chakra-ui/image';
import { Box, Center, Flex, Text, VStack, HStack } from '@chakra-ui/layout';
import { Spinner } from '@chakra-ui/spinner';
import React, { useEffect } from 'react';
import { getKDAStarRating } from './ChampionStats';
import StarTag from './tags/StarTag';

const getStarRatingStyle = (star) => {
  if (star < 1 || !star) { return { color: '#ababab' }; }
  else if (star < 2) { return { color: '#676767' }; }
  else if (star < 3) { return { color: '#90ee90' }; }
  else if (star < 4) { return { color: '#87cefa' }; }
  else if (star < 5) { return { color: '#ffa500', textShadow: '0px 0px 4px #ffa500' }; }
  else { return { color: '#ff4500', textShadow: '0px 0px 4px #ff4500' }; }
}

const getBorderStyle = (star) => {
  if (star < 2 || !star) { return {
    border: "1px solid black"
  }} else if (star < 3) { return {
    border: "3px solid #90ee90"
  }} else if (star < 4) { return {
    border: "5px inset #87cefa"
  }} else if (star < 5) { return {
    border: "7px groove #ffa500"
  }}
}

const IconBox = ({ profile_icon_id, level, totalKDA = null, performance = null, showStarRating = true }) => {
  return (
    <VStack mb={5}>
      { profile_icon_id ?
        <Box className="icon-box" boxSize="100px" mb={-2} style={getBorderStyle(((performance * 5) + getKDAStarRating(totalKDA)) / 2)}>
          <Image className="icon-box-image" src={`http://ddragon.leagueoflegends.com/cdn/11.5.1/img/profileicon/${profile_icon_id}.png`} />
          <Box className="icon-box-level-badge">
            {level}
          </Box>
        </Box>
        :
        <Flex align="center" justify="center" boxSize="100px" mb={-2}>
          <Spinner color="teal.500" />
        </Flex>
      }
      { showStarRating &&
        <Flex flexDirection="row">
          {/* {kdaStarRating(totalKDA, 5)} */}
          <StarTag style={getStarRatingStyle(((performance * 5) + getKDAStarRating(totalKDA)) / 2)} value={((performance * 5) + getKDAStarRating(totalKDA)) / 2} />
        </Flex>
      }
    </VStack>
  );
}

export default IconBox;