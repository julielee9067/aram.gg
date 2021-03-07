import { Image } from '@chakra-ui/image';
import { Box } from '@chakra-ui/layout';
import React, { useEffect } from 'react';

const IconBox = ({ profile_icon_id, level }) => {
  return (
    <Box className="icon-box" boxSize="100px" mb={10}>
      <Image className="icon-box-image" src={`http://ddragon.leagueoflegends.com/cdn/11.5.1/img/profileicon/${profile_icon_id}.png`} />
      <Box className="icon-box-level-badge">
        {level}
      </Box>
    </Box>
  );
}

export default IconBox;