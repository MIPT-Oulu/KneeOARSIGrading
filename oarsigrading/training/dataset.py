from torch.utils import data
from oarsigrading.dataset.utils import read_gs


class OARSIGradingDataset(data.Dataset):
    def __init__(self, metadata, img_trfs):
        super(OARSIGradingDataset, self).__init__()

        self.meta = metadata
        self.trf = img_trfs

    def __getitem__(self, idx):
        entry = self.meta.iloc[idx]
        img = read_gs(entry.fname)
        img_res, img_med, img_lat, kl_oarsi_grades = self.trf((img, entry))

        return {'img': img_res, 'img_med': img_med, 'img_lat': img_lat,
                'target': kl_oarsi_grades, 'ID': entry.ID,
                'SIDE': entry.SIDE, 'VISIT': entry.VISIT}

    def __len__(self):
        return self.meta.shape[0]
