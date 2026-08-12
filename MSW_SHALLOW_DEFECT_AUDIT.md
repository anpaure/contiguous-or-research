# The unchanged MSW factor has a macroscopic shallow-shadow defect

## 1. Question

The new integral component switches raised a possible shortcut: perhaps the
explicit Mütze--Standke--Wiechert factor already misses only
`O(Cat_m)=O(W/m)` targets at each fixed lower depth.  If so, its total defect
through a moderately growing band might be `o(W)` without any global
switching theorem.

This is false already at depth one.

## 2. Exact enumeration

For every Dyck word of semilength `m`, `msw_shadow_audit.cpp` reconstructs
the MSW omitted-label permutation from the published `g,h` maps.  It then
enumerates the `2m+1` alternating rank-`m-1` intervals of every selected
wreath and counts their distinct values.

The exact results are:

\[
\begin{array}{c|r|r|c}
m&\binom{2m+1}{m-1}&\text{missing}&\text{missing fraction}\\ \hline
4&84&4&0.047619\\
5&330&32&0.096970\\
6&1287&176&0.136752\\
7&5005&837&0.167233\\
8&19448&3709&0.190765\\
9&75582&15811&0.209191\\
10&293930&65860&0.224067\\
11&1144066&270337&0.236296
\end{array}
\]

The middle layer was independently verified to have multiplicity exactly
one in every case.  At `m=11`, the full rank-`m-1` multiplicity histogram is

\[
\begin{array}{c|rrrrrrr}
\text{multiplicity}&0&1&2&3&4&5&6\\ \hline
\text{targets}&270337&462000&352978&51434&6779&524&14.
\end{array}
\]

Thus the defect is not a small collection of exceptional Dyck boundaries.
It occupies a macroscopic fraction of the first lower layer.

The same run enumerated every lower depth through `m=11`.  For example, at
`m=11` the missing counts from ranks `10,9,...,2` are

\[
 270337,286787,197038,100863,38991,11086,2168,249,0.
\]

No asymptotic limit is claimed from this finite table.  The trend is
consistent with a positive limiting miss fraction at every fixed shallow
depth, rather than an `O(1/m)` fraction.

## 3. Consequence

The original MSW factor is an exact middle skeleton but not a low-excess
vertical factor.  Any proof of

\[
                         \nu(k)=(1+o(1))W(k)
\]

through this skeleton must use a positive-density family of integral
component switches, or replace the factor globally.  A Catalan-sized literal
repair of the unchanged factor cannot work even at the first lower rank.

The enumeration was run only on the remote RunPod in visible `tmux` session
`msw_vertical`; no enumeration was run on the Mac.  The exact command was

```text
./msw_shadow_audit 11 --all-depths
```

