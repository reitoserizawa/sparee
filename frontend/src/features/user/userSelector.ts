import type { RootState } from '../../apps/store';

export const selectLocation = (state: RootState) => state.user.location;
