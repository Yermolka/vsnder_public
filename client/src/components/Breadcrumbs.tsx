import { Breadcrumbs, Chip, emphasize, Link, styled } from "@mui/material";
import HomeIcon from '@mui/icons-material/Home';
import { Edit, Whatshot, Lock, Casino, ExitToApp } from "@mui/icons-material";


const breadcrumbToLink = [
    { name: "Смотреть всех", href: "/users", icon: <HomeIcon /> },
    { name: "Редактировать себя", href: "/edit", icon: <Edit /> },
    { name: "Изменить пароль", href: "/changePassword", icon: <Lock /> },
    { name: "Крутануть рулетку!", href: "/users/1", icon: <Casino /> },
    { name: "Выйти", href: "/logout", icon: <ExitToApp /> },
];

const StyledBreadcrumb = styled(Chip)(({ theme }) => {
    const backgroundColor =
      emphasize(theme.palette.primary.main, 0.12);
    return {
      backgroundColor,
      height: theme.spacing(3),
      color: theme.palette.text.primary,
      fontWeight: theme.typography.fontWeightRegular,
      '&:hover, &:focus': {
        backgroundColor: emphasize(backgroundColor, 0.20),
      },
      '&:active': {
        boxShadow: theme.shadows[1],
        backgroundColor: emphasize(backgroundColor, 0.12),
      },
    };
  }) as typeof Chip;

export function VSNBreadcrumbs() {
    return (
        <Breadcrumbs>
            {
                breadcrumbToLink.map(({ name, href, icon }) => {
                    return (
                            <StyledBreadcrumb 
                            key={name}
                            component="a"
                            href={href}
                            label={name}
                            icon={icon}
                            />
                        );
                })
            }
        </Breadcrumbs>
    )
}
