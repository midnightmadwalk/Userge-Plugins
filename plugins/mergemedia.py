"""MergeMedia"""
#  Copyright (C) 2020 BY USERGE-X
#  All rights reserved.
#
#  Author: https://github.com/midnightmadwalk [TG: @midnightmadwalk]


import os
import re

import shutil
from pathlib import Path

from userge import Message, userge
from userge.plugins.misc.upload import upload
from userge.utils import runcmd, progress

@userge.on_cmd(
    "mergesave",
    about={
        "header": "save file for {merge}",
        "usage": "{tr} reply to media ",
    },
)
async def mergesave_(message: Message):
  """mergesave"""
  # saving files in a separate folder.
  await message.edit("`downloading ...`", del_in=15)
  try:
      o_o = await message.client.download_media(message=message.reply_to_message, file_name='merge/', progress=progress, progress_args=(message, "`Saving for further merge !`"),
      )
  except AttributeError:
      await message.err("Reply To Media,dear.")
  else:
      await message.edit(f"Saved in {o_o}")


@userge.on_cmd(
    "merge",
    about={
        "header": "Merge Media.",
        "usage": "perform {tr}merge after saving videos with {tr}mergesave",
    },
)
async def merge_(message: Message):
    """MergeMedia with FFmpeg"""
    # preparing text file.
    await message.edit("`🙂🙃 Preparing text file ...`")
    x_x = open("merge.txt", "w+")
    for media in os.listdir("merge"):
        data_ = "file" +" "+ "'" + "merge/" + media + "'" +"\n"
        x_x.write(data_)
    x_x.close()
    # detecting extension.
    await message.edit("`😎🥲 detecting extension ...`")
    for ext in os.listdir("merge")[:1]:
        a_a, b_b = re.findall("[^.]*$", ext)
        output_path = "merge/output."+a_a
    await message.edit(f"detected extension is .{a_a}")
    # ffmpeg.
    await message.edit("`🏃️🏃 ffmpeg ...`")
    await runcmd(f"ffmpeg -f concat -i merge.txt -map 0 -c copy -scodec copy {output_path}")
    # upload.
    await upload(message, Path(output_path))
    # cleanup.
    await message.edit("`🤯😪 cleaning mess ...`", del_in=10)
    shutil.rmtree("merge")
    os.remove("merge.txt")
