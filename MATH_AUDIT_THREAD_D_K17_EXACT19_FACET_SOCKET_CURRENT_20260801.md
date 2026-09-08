# The `k=17` exact-19 facet socket has a positive endpoint-current signature, but its child cascade is not closed

Date: 2026-08-01  
Lane: Thread D / resident facet socket / endpoint current  
Status: exact solver-free replay of one frozen finite support certificate.  This
is a positive **finite signature**, not an all-parameter actuator theorem.

## 1. Current convention

For a directed Johnson arc `e=(X,Y)`, write

\[
 j_q(e)={\bf1}_{q\in X\cap Y}-{\bf1}_{q\in Y}.
\]

If `ins(e)` is the unique coordinate in `Y-X`, then

\[
                         j_q(e)=-{\bf1}_{q=\operatorname{ins}(e)}. \tag{1.1}
\]

Consequently, if a socket deletes the active old arcs `D` and inserts the
new arcs `N`, its exact endpoint-current change is

\[
 \boxed{\Delta\kappa_q=
   |\{e\in D:\operatorname{ins}(e)=q\}|-
   |\{e\in N:\operatorname{ins}(e)=q\}|.}          \tag{1.2}
\]

In particular,

\[
                         \sum_q\Delta\kappa_q=|D|-|N|. \tag{1.3}
\]

For a compact depth-`h` socket with `h+1` facets and two exterior
attachments, `|N|=h+2`.  Thus extraction counts alone determine only the
total in (1.3); the ordered insertion-label histograms are needed for every
coordinate cut.

## 2. Scope of the old compact catalogue

The exact support master has nineteen residual rank-ten colours.  Its SAT
certificate selects 4,862 minimum-residence component patterns and 1,419
cut colours.  The separate compact-socket table contains one resident
four-facet row for each residual colour, but each row was optimized
individually.  It did **not** require its exterior segments to belong to the
one frozen SAT pattern and did not enforce the global lower palette.

Replaying all nineteen `L=4` rows against the actual SAT-selected pattern
gives

\[
\begin{array}{c|c|c}
|D|&\sum_q\Delta\kappa_q&\#\text{ rows}\\ \hline
4&-1&11\\
5&0&5\\
6&+1&3.
\end{array}                                             \tag{2.1}
\]

Only three rows retain both advertised exterior segments in that same
pattern, for targets

\[
                         31418,\quad70398,\quad71658.    \tag{2.2}
\]

Among them only `U=70398` has positive total current.

## 3. The positive row

The literal owner sequence, including the two exterior endpoints, is

\[
82684\to70396\to70394\to70390\to70270\to67198.           \tag{3.1}
\]

The four facets of `U=70398` omit labels `(1,2,3,7)`.  Relative to the
frozen exact-19 pattern, extracting them deletes six active arcs.  Their
insertion labels are

\[
                         16,15,5,10,2,0.                  \tag{3.2}
\]

The five arcs in (3.1) insert

\[
                         12,1,2,3,10.                    \tag{3.3}
\]

Hence

\[
 \boxed{\Delta\kappa
   =e_{16}+e_{15}+e_5+e_0-e_{12}-e_1-e_3,}              \tag{3.4}
\]

with total current `+1`.  In the standard `m=9` convention `a=15` and
`z=16`, so

\[
                         \Delta\kappa_a=\Delta\kappa_z=1. \tag{3.5}
\]

Thus the finite socket escapes the neutral swapped-phase law at the level
of its signed incidence vector.

## 4. Lower-palette cleanup and upper-child debt

The row (3.1) is not yet a legal lower-injective replacement.  Its new
lower colours `70392` and `66174` are still used by retained old arcs:

\[
 (1049,3):71416\to70393,\qquad
 (452,5):66302\to98942.                                 \tag{4.1}
\]

These arcs insert labels `0` and `15`.  Releasing both makes the displayed
local lower palette collision-free and changes (3.4) to

\[
 \boxed{\Delta\kappa^{\rm clean}
   =e_{16}+2e_{15}+e_5+2e_0-e_{12}-e_1-e_3.}            \tag{4.2}
\]

Thus

\[
 \sum_q\Delta\kappa_q^{\rm clean}=3,\qquad
 \Delta\kappa_a^{\rm clean}+\Delta\kappa_z^{\rm clean}=3. \tag{4.3}
\]

This gain is paid for by three extra path components/repeat-upper units.
The new upper multiset is

\[
                   \{86780,70398,70398,70398,71294\}.    \tag{4.4}
\]

The two extra copies of `70398` and the duplicated retained exterior colour
`86780` are exactly the three repeat units.

After the two lower-provider releases, the unrepaired old upper colours are

\[
 \boxed{70391,71414,71417,71418,71420,99070,103164.}     \tag{4.5}
\]

Six have an extendable one-seam provider in the frozen atlas.  The colour

\[
                              \boxed{70391}              \tag{4.6}
\]

has none.  Therefore this finite row is not a closed facet actuator: it is
a positive-current root of another upper-provider cascade.

## 5. Exact conclusion

The compact facet socket can be non-neutral.  The exact-19 instance even
contains a row with simultaneous positive `a`- and `z`-current, and a
lower-clean formal extension with total gain three.  What the finite data
do **not** prove is simultaneous repair of (4.5), a connector realization
for the three additional components, graphic completion, deeper upper-deck
preservation, the lower compiler, or a supply theorem in general dimension.

The all-parameter question is therefore not whether a facet socket can have
positive current—it can—but whether positive rows admit a bounded closed
child cascade whose connector insertion labels avoid spending the gained
special-coordinate current.

## 6. Reproducibility

The solver-free audit is

`scratch/audit_threadD_k17_exact19_facet_socket_current_20260801.py`,

SHA-256 `6e003ce89a436b7606de98b9a7b3e41e6f0087f364835f85fddc5f8fd0d2582e`,

and its payload is

`scratch/threadD_k17_exact19_facet_socket_current_20260801.audit.json`,

SHA-256 `488df001343672938b4bbc19ff05b865f66e593f8ac3c19a4ba61ec6ded8777e`.

The audit replays the already verified SAT assignment; it performs no SAT
or exhaustive search.
