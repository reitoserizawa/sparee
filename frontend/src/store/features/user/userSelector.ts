import type { RootState } from '../../store/store';

export const selectLocation = (state: RootState) => state.user.location;
