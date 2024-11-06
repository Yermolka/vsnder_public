import { VsnderLocalStorage } from "../../../common/utils/common";

import { UserState } from "../states/user";
import { LOGIN_STATE_ITEM } from "./consts";

class UserInfoStorage extends VsnderLocalStorage<UserState> {}

export const userInfoStorage = new UserInfoStorage(LOGIN_STATE_ITEM);
