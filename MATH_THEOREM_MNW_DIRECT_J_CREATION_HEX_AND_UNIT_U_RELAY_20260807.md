# The direct `J`-creation face is a third unit-hole relay

**Date:** 2026-08-07  
**Method:** exact MSW touching-step phases and exact inverse multiplicities;
no computation or search  
**Status:** unconditional local theorem in the canonical-plus-gamma-alpha,
two-boundary-hex state.  The displayed face tensors over every Dyck suffix.
It creates the missing `J` target but moves the unique q2 hole to a new
target `U`; it is not a closed repair.  Extension of the three prepared
faces to one MNW spanning hypertree is not asserted here.

## 1. Input state

After the leaf transfer and its unique boundary-restoring companion, the
boundary incidences are restored and the net q2 current of those two faces
is

\[
 [A]-[J],\qquad
 A=1010101111,\qquad J=1100101111.                  \tag{1.1}
\]

The target `A` has canonical multiplicity two.  The target `J` has the
unique canonical inverse witness `(5,9)`, and that witness is precisely the
one removed by the second boundary face.  Thus `J` is the only q2 casualty
of (1.1).

## 2. A direct alternating face creating `J`

Put

\[
 Z=1100100101,\qquad K=Z-5=1100000101.              \tag{2.1}
\]

Use the active labels `5,6,9`.  The three lower owners are

\[
\begin{aligned}
 Z   &=K+5=1100100101,\\
 Z_6 &=K+6=1100010101,\\
 Z_9 &=K+9=1100000111,
\end{aligned}                                       \tag{2.2}
\]

and the three upper colours are

\[
\begin{aligned}
 P&=K+56=1100110101,\\
 N&=K+69=1100010111,\\
 Q&=K+59=1100100111.
\end{aligned}                                       \tag{2.3}
\]

The exact touching-step rule gives the following selected additions in the
current partial factor:

\[
\begin{array}{c|c|c}
\text{owner}&\text{selected additions}&\text{selected/unselected face edges}\\ \hline
Z   &\{6,7\}&P\text{ selected},\ Q\text{ unselected},\\
Z_6 &\{7,9\}&N\text{ selected},\ P\text{ unselected},\\
Z_9 &\{4,5\}&Q\text{ selected},\ N\text{ unselected}.
\end{array}                                         \tag{2.4}
\]

None of these three owners or six incidences belongs to the gamma-alpha
pair or the two boundary faces.  Hence their canonical phases persist in
the partial factor.  The six statuses alternate, so toggling this incidence
hexagon is literal and q1-degree preserving.

At `Z` it replaces addition six by addition nine while retaining addition
seven.  The new turn is therefore

\[
 Z+\{7,9\}=1100101111=J.                            \tag{2.5}
\]

## 3. Exact q2 current

At the three owners the turns change as

\[
\begin{array}{c|c|c}
\text{owner}&\text{old turn}&\text{new turn}\\ \hline
Z   &1100111101&1100101111,\\
Z_6 &1100011111&1100111101,\\
Z_9 &1101100111&1101010111.
\end{array}                                         \tag{3.1}
\]

The intermediate target cancels.  With

\[
 U=1100011111,\qquad
 W=1101100111,\qquad
 V=1101010111,                                      \tag{3.2}
\]

the signed current is

\[
 \boxed{\partial_2 H_J=[J]+[V]-[U]-[W].}            \tag{3.3}
\]

The exact inverse witnesses are

\[
\begin{array}{c|c|c}
\text{target}&\text{canonical inverse witnesses}&\text{multiplicity}\\ \hline
U&(7,9)&1,\\
W&(4,5),(8,9)&2,\\
V&(8,9)&1.
\end{array}                                         \tag{3.4}
\]

For example, for `U` the down-step at position three is the sole
height-two barrier.  Only the late productive chamber survives, and its
left and right ordinal labels agree only for `(7,9)`.  The corresponding
owner is exactly `Z_6`, so this is an internal, rather than endpoint,
witness.  The other two rows follow from the same chamber test.

None of `U,V,W` occurs in the signed currents of the gamma-alpha pair or
the two boundary faces.  Their loads immediately before `H_J` are therefore
the canonical loads (3.4).  Toggling `H_J` fills `J`, raises `V` from one
to two, lowers `W` from two to one, and lowers `U` from one to zero.

Combining (1.1) and (3.3) gives

\[
 \boxed{[A]+[V]-[U]-[W].}                           \tag{3.5}
\]

Thus the only new q2 hole is `U`.  The third face is an exact one-unit hole
relay, not a closure.

## 4. Direct-creation classification in this state

Any single incidence face creating `J` must do so at a lower owner

\[
                         J-\{p,q\},                 \tag{4.1}
\]

where exactly one of additions `p,q` is currently selected.  The
touching-step rule leaves the following complete list.  The middle column
is the current selected pair at the centre; `reverse H_2` denotes the
boundary-destroying reversal of the second face.

\[
\begin{array}{c|c|c}
\{p,q\}&\text{selected pair at }J-\{p,q\}&
 \text{admissible completion core}\\ \hline
\{1,10\}&\{3,10\}&\varnothing\\
\{2,5\}&\{2,3\}&\varnothing\\
\{2,7\}&\{2,3\}&\varnothing\\
\{2,8\}&\{2,3\}&\varnothing\\
\{2,9\}&\{3,9\}&\varnothing\\
\{2,10\}&\{2,3\}&\varnothing\\
\{5,7\}&\{4,5\}&\varnothing\\
\{5,8\}&\{4,5\}&\varnothing\\
\{5,9\}&\{3,5\}&\text{reverse }H_2\\
\{5,10\}&\{4,5\}&\varnothing\\
\{7,9\}&\{6,7\}&5.
\end{array}                                         \tag{4.2}
\]

All other pairs have either zero or two desired selected incidences and
cannot create `J` by changing one incidence at the centre.  For each row
of (4.2), the five possible core labels are the five labels of the centre.
The two auxiliary touching-step tests eliminate them exactly as recorded.
One instructive near miss is `\{5,8\}`: core nine would alternate in the
canonical factor, but its auxiliary owner is the unique provider
`1100001101`; the second boundary face has already changed its selected
pair from `\{5,9\}` to `\{3,5\}`.  Hence it is unavailable in the state in
which `J` is actually missing.

Therefore (apart from undoing the boundary restoration) (2.1)--(2.4) is
the only direct `J`-creation incidence hex in this partial factor.

## 5. Dyck suffixing and scope

Append any Dyck word `v` to every owner, colour, and turn above.  The MSW
path recursion concatenates, so all six incidence phases in (2.4) persist.
Every target in (3.1) ends at height four, and a Dyck suffix read from
height four adds no eligible low/high inverse position.  Hence the
multiplicities in (3.4) remain exact.

Distinct suffixes give disjoint incidence tensors.  Consequently the full
bank `\{H_Jv\}` can be toggled simultaneously and transports the cylinder
of holes

\[
                         Jv\longmapsto Uv.           \tag{5.1}
\]

This theorem is local.  It proves neither that these faces are members of
one selected MNW spanning hypertree nor that their component actions cancel
with the annulus sweep.  The exact next signed target is the cylinder

\[
                         \boxed{1100011111v}.         \tag{5.2}
\]
