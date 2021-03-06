#  Copyright (c): Wenyi Tang 2017-2019.
#  Author: Wenyi Tang
#  Email: wenyi.tang@intel.com
#  Update Date: 2019/4/3 下午5:10

import numpy as np
import torch


def psnr(x, y, max_val=1.0):
  if isinstance(x, torch.Tensor):
    x = x.detach().cpu().numpy()
  if isinstance(y, torch.Tensor):
    y = y.detach().cpu().numpy()
  mse = np.square(x - y).mean()
  return 10 * np.log10(max_val ** 2 / mse)


def total_variance(x, reduction='mean'):
  hor = x[..., :-1, :] - x[..., 1:, :]
  ver = x[..., :-1] - x[..., 1:]
  if isinstance(x, torch.Tensor):
    tot_var = torch.sum(torch.abs(hor)) + torch.sum(torch.abs(ver))
  elif isinstance(x, np.ndarray):
    tot_var = np.abs(hor).sum() + np.abs(ver).sum()
  if reduction == 'mean':
    reduce = x.shape[-1] * x.shape[-2]
  else:
    reduce = 1
  return tot_var / reduce
