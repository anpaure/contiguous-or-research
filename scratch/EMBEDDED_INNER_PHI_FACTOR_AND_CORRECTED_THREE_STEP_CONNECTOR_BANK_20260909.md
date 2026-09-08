# An embedded smaller carrier supplies the corrected three-step connector bank

Date: 2026-09-09. Pure conditional construction; no execution or search.

The input here is an **actual specified strict canonical-Phi factor with
residence at least3** on2r−1 coordinates. An optimal word in that dimension
alone is not asserted to supply this input. In particular no unverified
residence claim about a17-coordinate carrier is assumed.

The construction embeds that factor, cuts its fixed-root edges, and appends
explicit age-legal three-step connectors. It gives a path cover with exact
free ports. It does not complete the child factor or coexist automatically
with a retained outer parent copy.

## 1. Input, labels, and the retained embedding theorem

Let r>=2. Let sigma be the successor permutation of a complete strict
canonical-Phi factor on2r−1 inner sites, with lower rankr−1. Assume its
positive lower-coordinate runs have length at least3. Its total lower
inventory is

\[
M'=\binom{2r-1}{r-1}.
\]

Place two new fixed zeros before the inner word X and two fixed ones after
it. The child lower state is `00X11`, of rankr+1 on2r+3 sites. Call the first
two coordinates u,x, the first inner coordinate y, and the final coordinates
a,b. The child outer-sector notation refers to a,b.

The earlier [balanced Dyck-block embedding, Section3](CANONICAL_PHI_BALANCED_BLOCK_BARRIER_AND_MINIMAL_RUN_SECTOR_EXCURSION_20260909.md)
already proves matching preservation. Here the block1100 lies across the
cyclic cut. Equivalently, in the displayed linear reading the first two
zeros shift every inner height by−2, while the final two ones cannot create
a lower first minimum. Hence

\[
\Phi_{child}(00X11)=00\Phi_{inner}(X)11.
\]

Every original edge embeds as `00X11 -> 00sigma(X)11`. The inner ages evolve
exactly as in the supplied factor, a,b are permanently present, and u,x
permanently absent. This supplies a genuine cyclic age history and gives
**no amplification of inner residence**.

## 2. The cut ports and their explicit connector

The inner fixed-root states are `X=0D`, with D a Dyck word of semilengthr−1.
There are

\[
h'=\mathrm{Cat}_{r-1}
\]

such states. Since r>=2, D is nonempty and begins with1; write `D=1R`.
At each root, remove the original embedded edge

\[
000D11\longrightarrow00\sigma(0D)11
\]

and install the following three edges:

\[
\boxed{
T_0=000D11\longrightarrow
T_1=001D10\longrightarrow
T_2=011D00\longrightarrow
T_3=1110R00.}
\tag{2.1}
\]

The successive inserted coordinates are y,x,u. The successive deletions are
b,a,d, where d is the first one of D (the first position of the displayedR
prefix is not deleted).

All insertions are canonical. At T_0 the old height first reaches−3 at y;
at T_1 it first reaches−2 at x; at T_2 it first reaches−1 at u. The consumed
uppers are, respectively,

\[
001D11,\qquad011D10,\qquad111D00.
\tag{2.2}
\]

The first is the original embedded outgoing upper of the cut root and is
reused, not counted twice. The other two are new upper10 and upper00 states.

## 3. Ages inherited from the specified smaller factor

At T_0, a,b have the permanent-present history of the embedding. The D-ones
have their actual inner ages, each at least1. Therefore:

* The first edge legally deletes b, which is already mature.
* The second legally deletes a, also already mature.
* The third deletes d only after it has survived T_0,T_1,T_2, so its age at
  deletion is at least3, regardless of its particular initial inner age.

The newly inserted y,x,u are not deleted by the connector. At T_3 they have
exact ages3,2,1, respectively. Every other present inner coordinate has its
initial age plus3, hence age at least4. Thus the terminal old prefix111 has
ages `(1,2,3)` in coordinate order u,x,y; all remaining present coordinates
are mature for residence3. Both new coordinates are absent.

This is also the concrete instance of the
[forced plateau deletion rule](CANONICAL_PHI_BACKWARD_AGE_OBLIGATIONS_AND_INITIAL_PLATEAU_THEOREM_20260909.md):
at `011D00`, its first two ones are too young, whereas every D-one is old
enough. Deleting the first D-one gives the injective corrected head1110R.

Cutting the cyclic input does not magically give a new global incoming
history at each exposed path head. A sufficient explicit boundary certificate
for later gluing is: at `00sigma(0D)11`, a,b have age at least3 and every
present inner coordinate has age at least its original inner age capped at3.
Along the retained inner path, age dominance is preserved by the identical
insertions and deletions. These boundary data therefore validate the entire
retained path and its connector. They are actual inherited data from the
specified embedded factor, and remain requirements on any replacement
incoming connection; they are not freely assigned mature ages.

## 4. All vertices and consumed uppers are distinct

The original embedded states have outer sector11 and old initial bits00.
The three new lower banks have the following distinguishing prefixes:

|Bank|Outer sector|Old prefix|
|---|---|---|
|T_1=001D10|10|001|
|T_2=011D00|00|011|
|T_3=1110R00|00|1110|

Thus they are mutually disjoint and disjoint from the embedded inventory.
Each map from D into a bank is injective; for T_3 the fixed prefix recoversR
and henceD. The consumed new upper banks are in sectors10 and00, whereas
all embedded outgoing uppers are in sector11. They are injective and mutually
disjoint. Alternatively, global upper distinctness follows from the
injectivity of canonical Phi on the distinct outgoing lower states.

There is no edge-level or vertex-level collision **within this specified
embedded factor plus connector bank**. This statement does not include
other old partial constructions.

## 5. Exact path-cover and free-port accounting

Remove all h' root outgoing edges from the inner factor. On every component
containing roots this produces one directed path per cut, beginning at a
head `00sigma(0D)11` and ending at some cut root `000D_1 11`. Append that
root's connector. The result is exactlyh' open paths, together with any
untouched inner components that contain no roots. If the supplied inner
factor is Hamilton, there are no such untouched components.

The full accounting is

\[
\begin{aligned}
\text{used lower states}&=M'+3h',\\
\text{assigned edges / consumed uppers}&=M'+2h'.
\end{aligned}
\tag{5.1}
\]

Indeed h' old edges are removed and3h' connector edges added. Three outside
lower states per root are new, while only two consumed uppers per root are
new. The exact remaining used-inventory ports are:

* **Missing incoming heads:** `00sigma(0D)11`, one for each original root.
* **Free outgoing lower ends:** `1110R00`, one for each rootD=1R.
* **Their free outgoing uppers:** `1110R01`.

For the last formula, all nonempty old prefixes of1110R are strictly
positive: R has prefix height at least−1, so after1110 the old heights
remain at least1. The new zeros first reach0 and then−1; canonical Phi
therefore inserts b. These free uppers have not been consumed elsewhere.

The terminal upper lacks a, whereas every missing incoming head contains
a. Consequently these open paths cannot be closed merely by matching the
listed free uppers directly to the listed heads. Further states or changed
incidences are needed. The retained root-free cycles would also need an
additional cut to join a single eventual global component.

In the complete child middle layer of size `W_child=binom(2r+3,r+1)`, let
V be the used lower inventory and S the consumed upper inventory. The exact
unassigned incidence classes are

\[
\begin{aligned}
\text{upper side}&=\{\text{all child uppers}\}\setminus S,\\
\text{lower side}&=(\{\text{all child lowers}\}\setminus V)
                 \cup\{00\sigma(0D)11\}.
\end{aligned}
\]

Both have size `W_child−M'−2h'`. Incidence, exclusion of a Phi self-return,
and the stated age boundary are necessary for any continuation. No matching
in this residual graph is asserted or searched for.

## 6. Compatibility boundaries and the input gate

The new T_1 states belong to an outer parent10 copy if such a copy is also
retained: their old masks001D have rankr. Thus they can collide with that
copy. The embedded sector11 inventory can also overlap a previous q3
second11 bank. The proof supplies no disjointness from either structure;
those inventories cannot be combined without an explicit allocation check.

The bank uses supplied inner ages and only preserves residence3. It neither
manufactures a residence3 inner factor from an optimal word nor increases
the residence parameter. For child21, a suitable17-coordinate inner carrier
is therefore an additional input gate unless separately verified.

The positive result is a conditional, explicit, globally disjoint path bank
with correct inherited ages and a complete free-port ledger. It replaces
the invalid wholesale all-root entrance installation with different source
pieces. It is not a full child factor, a universal ordinary word, or an
all-dimensional equality proof.

## 7. Independent review

Root read the complete note and passed it. The induction agent independently
read the full proof and passed the matching commutation, inherited ages,
lower/upper disjointness, path ledger, and free-upper obstruction. Both
reviews retain the conditional smaller-carrier input and the explicit
boundary-age requirements. No execution was used.
