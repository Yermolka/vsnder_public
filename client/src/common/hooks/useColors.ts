import { useTheme } from '@mui/material';

import { PRIMARY_COLOR, SECONDARY_COLOR } from '../../common/consts/common';
import { alphaColor, colorsLinearGradient, darkenColor, lightenColor } from '../../common/utils/color';

export interface AppColors {
  iconColor: string;
  iconTextColor: string;
  authLinkColor: string;
}

export function useColors() {
  const theme = useTheme();
  const authLinkColor = theme.palette.mode === 'dark' ? theme.palette.grey.A400 : theme.palette.grey[600];

  const primaryAlphaColor = alphaColor(PRIMARY_COLOR, 0.9);
  const secondaryAlphaColor = alphaColor(SECONDARY_COLOR, 0.9);

  const primaryIconColor = primaryAlphaColor;
  const primaryIconTextColor = theme.palette.getContrastText(primaryIconColor);

  const secondaryIconColor = secondaryAlphaColor;
  const secondaryIconTextColor = theme.palette.getContrastText(secondaryIconColor);

  const searchBarBackground =
    theme.palette.mode === 'light' ? lightenColor(SECONDARY_COLOR, 0.85) : darkenColor(SECONDARY_COLOR, 0.85);

  const menuBackground =
    theme.palette.mode === 'light' ? lightenColor(PRIMARY_COLOR, 0.85) : darkenColor(PRIMARY_COLOR, 0.85);

  const purplePinkAlphaGradient = colorsLinearGradient(primaryAlphaColor, secondaryAlphaColor);

  return {
    primaryIconColor,
    secondaryIconColor,
    primaryIconTextColor,
    secondaryIconTextColor,
    authLinkColor,
    purplePinkAlphaGradient,
    menuBackground,
    searchBarBackground,
  };
}
