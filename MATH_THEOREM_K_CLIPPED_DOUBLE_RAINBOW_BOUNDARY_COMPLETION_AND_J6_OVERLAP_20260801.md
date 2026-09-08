# The clipped double-rainbow comparator: corrected literal source, exact Boundary Completion, and a J6 overlap

Date: 2026-08-01  
Lane: K, global boundary completion  
Status: unconditional audit/correction of the local comparator; exact
necessary-and-sufficient owner/upper completion reduction; unconditional
one-ended overlap with the resident pivot/J6 path and an exact obstruction
to the direct right return.  The existence of an upper-complete spanning
middle chronology and its terminal lower compiler remain open.  No
`B(k)+O(1)` or `B(k)` conclusion is claimed.

## 0. Scope and verdict

This note audits lines 1--760 of the supplied `pasted-text.txt`, whose SHA is

```text
ff3c49f136d53b5c650434627948d95e0246ee808b743c4b1952f966f3e2c976.
```

The displayed two-ended construction is almost correct, but its assertion
of a **literal** lower-`q1` rainbow has one defect.  At the central
`p_L -> p_R` transition the abstract owner intersection is

\[
             K\cup\{a_1,a_3\}\cup F,
\]

whereas the shared depth-`d-1` source block has OR only `F`.  One common
base-loading of a bridge cell repairs this at zero length and without
changing any owner, ray, or strict-upper occurrence.

After that repair the following local assertions are exact.

1. The two phases have the same simple rank-`r` Johnson owner path.
2. Their lower and upper immediate palettes are literal and separately
   injective.
3. Their signed occurrence difference consists of exactly `d-1` left
   prefixes and `d-1` right suffixes, all of rank at most `r-2`.
4. Every internal owner run has length at least `d+1`; this is a **clipped
   linear** statement, not a cyclic one.
5. The two-boundary threshold pairs are exactly `(0,j)` and `(j,0)`, so the
   abstract terminal birail defect is zero.

The attachment's proposed Boundary-completion implication is logically
valid, but replacing its short bridge by an arbitrary common middle word
does not inherit the local Johnson, residence, or literal-lower proofs.
The global problem has an exact sharper form:

> choose an owner permutation extending the two fixed collars, satisfying
> a clipped maximal-erosion/cap condition and consecutive-block upper
> surjectivity; then solve the lower compiler inside those caps.

The maximal common middle word is forced once the owner order is fixed.
Thus the owner/upper search can be carried out entirely in owner space.

Finally, the left collar overlaps the authenticated resident J6 path
literally for every `d`.  At `k=17` a filler relabelling gives a fully
double-rainbow, residence-clean overlap.  Direct attachment of the right
collar then creates a rank-ten owner, so a genuine source-history rethread
is still necessary.

## 1. Audit of the local comparator

Use the notation of the attachment.  Put

\[
 B_0=K\cup\{a_1,a_3\},\qquad
 g_i=f_{d+1-i}.
\]

The left source word is

\[
\begin{split}
L_\varepsilon^\sigma=(&Z_\varepsilon^L,
 f_2,\ldots,f_{d-1},H_L,\ell,
 c_{\sigma(1)},\ldots,c_{\sigma(d-2)},J_L^\sigma,Q_L),
\end{split}                                                    \tag{1.1}
\]

where

\[
\begin{aligned}
 Z_\varepsilon^L&=K\cup\{z,x_\varepsilon,f_1\},
       &x_0&=a_3,&x_1&=a_1,\\
 H_L&=K\cup\{a_1,a_3,f_1,\ell\},\\
 J_L^\sigma&=K\cup\{a_1,a_3,c_{\sigma(d-1)}\},\\
 Q_L&=K\cup\{a_1,a_3,p_L\}.
\end{aligned}                                                \tag{1.2}
\]

The right word is the reversed copy with `f_i -> g_i`,
`ell -> rho`, `p_L -> p_R`, and phase markers
`y_0=a_1,y_1=a_3`.  The original common bridge is

\[
                         G=(g_1,\ldots,g_d).             \tag{1.3}
\]

Thus `|L|=|R|=2d+1`, `|G|=d`, and the complete local source has
length `5d+2`.  Its depth-`d` row has `4d+2` owners.

### Theorem 1.1 (owner and abstract-palette audit)

The depth-`d` row of `L || G || R` is phase-independent.  Its `4d+1`
successive Johnson exchanges are exactly

\[
\begin{array}{ll}
z\to c_{\sigma(1)},&
f_i\to c_{\sigma(i)}\ (2\le i<d),\quad f_1\to p_L,\\
\ell\to g_1,&
c_{\sigma(i)}\to g_{i+1}\ (1\le i<d),\\
p_L\to p_R,\\
g_i\to c_{\tau(d-i)}\ (1\le i<d),&g_d\to\rho,\\
p_R\to g_1,&
c_{\tau(i)}\to g_i\ (2\le i<d),\quad c_{\tau(1)}\to z.
\end{array}                                                \tag{1.4}
\]

Every owner has rank `r`, the owners are distinct, and their abstract lower
and upper edge colours are separately injective.

#### Proof

There are `d,d,1,d,d` exchanges in the five displayed regions.  Sliding the
window through the left word gives

\[
 T_0^L=K\cup\{z,a_1,a_3,\ell\}\cup F[1,d-1]
\]

and then removes `z,f_2,...,f_(d-1),f_1` while inserting
`c_(sigma(1)),...,c_(sigma(d-1)),p_L`.  The bridge removes
`ell,C` and inserts `g_1,...,g_d`; the two common endpoint screens make the
central exchange `p_L -> p_R`.  The reversed calculation gives the right
half.  This proves (1.4) and the rank claim.

Within each region the accumulated `C` and filler subsets change
monotonically.  Across regions the lower edge intersections have marker
signatures

\[
          \{\ell\},\quad\{p_L\},\quad\varnothing,
          \quad\{p_R\},\quad\{\rho\}.                 \tag{1.5}
\]

They are therefore distinct.  The upper argument is identical except at
the two bridge junctions; there the possible colours differ by
`f_1` versus `f_d`, which are distinct because `d>=2`.  The notation
`(p_L,p_R)` in the attachment is an upper-edge signature, not an owner
signature.  This proves the theorem. \(\square\)

### Lemma 1.2 (the exact literal-`q1` identity)

For an arbitrary source word `A`, put

\[
 T_i=\bigcup_{j=i}^{i+d}A_j,qquad
 Q_i=\bigcup_{j=i+1}^{i+d}A_j.
\]

Then

\[
 T_i\cap T_{i+1}=Q_i\cup(A_i\cap A_{i+d+1}),          \tag{1.6}
\]

while

\[
 T_i\cup T_{i+1}=\bigcup_{j=i}^{i+d+1}A_j.           \tag{1.7}
\]

Hence the upper edge colour is always a literal interval.  The lower edge
colour is literal at its natural shared address iff

\[
                 A_i\cap A_{i+d+1}\subseteq Q_i.      \tag{1.8}
\]

#### Proof

Equation (1.6) is the distributive identity

\[
 (A_i\cup Q_i)\cap(Q_i\cup A_{i+d+1})
 =Q_i\cup(A_i\cap A_{i+d+1}),
\]

and (1.7) is immediate. \(\square\)

At the central edge of the unmodified bridge,

\[
\begin{aligned}
 O_L&=B_0\cup\{p_L\}\cup F,\\
 O_R&=B_0\cup\{p_R\}\cup F.
\end{aligned}                                                \tag{1.9}
\]

Thus \(O_L\cap O_R=B_0\cup F\), but \(Q_i=\operatorname{OR}(G)=F\).  Every extension of
`G` to the left or right acquires `p_L` or `p_R`, so the missing colour is
not another displayed interval.  This is the unique literal defect.

### Proposition 1.3 (one-cell, zero-length repair)

Replace the first bridge singleton `{g_1}` in both phases by

\[
                         B_0\cup\{g_1\}.               \tag{1.10}
\]

Then every owner and every upper interval remains unchanged, every lower
edge colour is literal, and the phase-to-phase ray relation is unchanged.

#### Proof

Every owner window containing this bridge address already contains `B_0`
through `Q_L` or `Q_R`, so (1.10) changes no owner.  Every noncentral shared
`d`-block containing it already contains one of those screens.  The central
shared block changes from `F` to `B_0 union F`, exactly (1.9).

The only absolute interval values changed by (1.10) are

\[
                   (g_1),\ (g_1,g_2),\ldots,(g_1,\ldots,g_d).
\]

Their new ranks are

\[
 |K|+2+j=r-d-1+j\le r-1\qquad(1\le j\le d).          \tag{1.11}
\]

Thus no owner or strict-upper occurrence changes.  The repair is common to
both phases and lies outside the endpoint rays. \(\square\)

### Proposition 1.4 (exact ray and residence scope)

Only the first and last source letters depend on the phase.  The complete
signed occurrence difference is

\[
\begin{split}
\mathfrak D({\cal C}_0)-\mathfrak D({\cal C}_1)
={}&\sum_{j=1}^{d-1}
 ([Kza_3F[1,j]]-[Kza_1F[1,j]])\\
&+\sum_{j=2}^{d}
 ([Kza_1F[j,d]]-[Kza_3F[j,d]]).                       \tag{1.12}
\end{split}
\]

There are `2d-2` changed physical addresses and `4d-4` signed atoms.  Every
changed value has rank at most `r-2`.  Therefore all rank-`(r-1)` and higher
occurrence multisets agree phasewise.

Every internal positive coordinate run in the owner path has length at least
`d+1`.  This is clipped residence only: `z` has a length-one run at each
global end, and cyclically joining the two ends gives length two, which is
short for `d>=2`.

#### Proof

An interval containing the first source position is a prefix.  Once it
reaches `H_L` it contains both phase labels.  Hence precisely the first
`d-1` prefixes change.  The suffix argument is symmetric.  The rank bound
is

\[
 (r-d-3)+2+(d-1)=r-2.
\]

For residence, an occurrence of a coordinate at source address `p` covers
the owner interval `[p-d,p]`, clipped to the owner index set.  Every
nonboundary connected component of a union of such length-`d+1` intervals
has length at least `d+1`. \(\square\)

The ambient support count is `r+d+3`.  The attachment's central-binomial
argument correctly proves `d<=m-3` for `m=floor(k/2)>=6`, so the local
source fits.  Its threshold pairs are

\[
             (0,j),(j,0)\qquad(1\le j<d),             \tag{1.13}
\]

and therefore `C(a,c)=a+c` at every critical corner.  This proves abstract
birail defect zero, but not a physical terminal matching in an ambient cap.

## 2. Strict-upper language is exactly an owner-order property

Let a nonzero source word have length `W+d`, and put

\[
                 T_i=\bigcup_{j=i}^{i+d}A_j
                 \qquad(0\le i<W).                    \tag{2.1}
\]

Assume every `T_i` has rank `r`.

### Theorem 2.1 (consecutive-block union equivalence)

Every source interval of length at most `d` is contained in some owner
`T_i`.  For every source interval of length at least `d+1`,

\[
       \bigcup_{j=p}^{q}A_j
       =\bigcup_{i=p}^{q-d}T_i.                        \tag{2.2}
\]

Conversely every nonempty consecutive block of owners is the OR of one
source interval:

\[
       \bigcup_{i=a}^{b}T_i
       =\bigcup_{j=a}^{b+d}A_j.                        \tag{2.3}
\]

Consequently the word covers every strict-upper target iff

\[
 \forall U\subseteq[k],\ |U|>r,\quad
 U=T_a\cup T_{a+1}\cup\cdots\cup T_b                 \tag{2.4}
\]

for some consecutive owner block.  This criterion depends only on the
owner order, not on the choice of inverse source word.

#### Proof

If `[p,q]` has at most `d` positions, choose

\[
 i\in[\max(0,q-d),\min(p,W-1)].
\]

The interval is contained in owner window `[i,i+d]`, so its OR has rank at
most `r`.  If `q-p+1>=d+1`, the owner windows with starts
`p,...,q-d` cover exactly the source positions `p,...,q`, proving (2.2).
Equation (2.3) is the same identity reversed.  A strict-upper target cannot
come from a short source interval, and (2.2)--(2.3) finish the proof.
\(\square\)

This theorem is the exact long-window part of Boundary Completion.  It also
separates the problem cleanly:

* owner coverage is the permutation row;
* strict-upper coverage is consecutive-block union surjectivity;
* strict-lower coverage uses only source intervals of length at most `d`.

## 3. Exact common-middle criterion

Fix the two collars `L_epsilon,R_epsilon` at the first and last `2d+1`
source addresses, and let `V` be the intervening `W-3d-2` addresses.  At a
fixed address `j` write `B_j^epsilon` for its prescribed collar letter.
For a proposed common owner order `T=(T_0,...,T_(W-1))`, define

\[
 I_j=[\max(0,j-d),\min(W-1,j)]                        \tag{3.1}
\]

and its maximal cap

\[
                         E_j(T)=\bigcap_{i\in I_j}T_i. \tag{3.2}
\]

This is the fixed-collar specialization of the screened maximal-erosion
criterion in
`MATH_THEOREM_THREAD_D_BOUNDARY_COATOM_RAIL_COMMONQ_MAXIMAL_EROSION_20260801.md`.

### Theorem 3.1 (common-middle iff)

There is one common nonzero middle word `M` such that

\[
 D^d(L_0||M||R_0)=D^d(L_1||M||R_1)=T               \tag{3.3}
\]

iff all of the following hold.

1. For every fixed address and both phases,
   \[
                         B_j^\varepsilon\subseteq E_j(T). \tag{3.4}
   \]
2. Every variable cap is nonempty:
   \[
                         E_j(T)\ne\varnothing\qquad(j\in V). \tag{3.5}
   \]
3. For every owner row `i` and both phases,
   \[
   T_i=
   \bigcup_{\substack{j\in[i,i+d]\\j\notin V}}B_j^\varepsilon
   \ \cup\
   \bigcup_{\substack{j\in[i,i+d]\\j\in V}}E_j(T). \tag{3.6}
   \]

When these conditions hold, the canonical witness is

\[
                         M_j=E_j(T)\qquad(j\in V).     \tag{3.7}
\]

#### Proof

Every source letter at address `j` belongs to every owner window using that
address, so it is contained in `E_j(T)`.  This proves (3.4) and shows that
any feasible variable letter lies in its cap.  Nonzeroness gives (3.5).

If a feasible middle exists, enlarge every variable letter to `E_j(T)`.
Each added coordinate still belongs to every owner that sees the address,
so no union can exceed its prescribed `T_i`; the old letters already cover
`T_i`.  Hence (3.6) holds.  Conversely (3.4)--(3.6) say directly that the
word with (3.7) has derivative `T` in both phases. \(\square\)

Thus the owner/upper search has no separate `M` variable: search for `T`,
test (3.4)--(3.6), and take maximal caps.  Source-cell thinning inside
those caps remains available for the terminal lower compiler and does not
change the owner order or its strict-upper language.

### Corollary 3.2 (correct Boundary-completion implication)

Suppose a rank-`r` owner permutation `T` satisfies Theorems 2.1 and 3.1.
Suppose its consecutive blocks miss at most `C_U` strict-upper targets, and
some common subcap middle source assigns the canonical rays and admits a
matching of distinct short intervals missing at most `C_L` strict-lower
targets in one terminal phase.  Then

\[
                         \nu(k)\le B(k)+C_U+C_L.       \tag{3.8}
\]

In particular `C_U,C_L<=C` gives `B(k)+2C`.

#### Proof

The owner row covers every rank-`r` target.  Theorem 2.1 supplies the stated
strict-upper targets and the terminal matching supplies the stated
strict-lower targets.  Append each missing target once as a literal source
letter.  Appending destroys no old witness. \(\square\)

This validates the implication in the attachment.  It does not prove its
hypotheses.

### Proposition 3.3 (literal lower colours under maximal erosion)

On an edge whose `d` shared source addresses all use maximal caps, clipped
`d`-residence of the coordinate traces implies

\[
               \bigcup_{j=i+1}^{i+d}E_j(T)=T_i\cap T_{i+1}. \tag{3.9}
\]

Thus lower `q1` is automatic there.  Fully fixed collar edges and mixed
interfaces still require the direct test (1.8).

#### Proof

Fix \(x\in T_i\cap T_{i+1}\) and let `[s,e]` be its positive trace run.
For an internal run, `e-s+1>=d+1`.  The intervals

\[
                  [s+d,e]\quad\text{and}\quad[i+1,i+d]
\]

intersect; any address in the intersection has an incident owner interval
contained in `[s,e]`, hence its maximal cap contains `x`.  If the run is
left-clipped choose address `i+1`; if it is right-clipped choose `i+d`.
The reverse containment is automatic from (3.2). \(\square\)

The residence hypothesis is essential.  For example, at `d=2` the owner
Hamilton path

\[
                 12,13,23,24,14,34                    \tag{3.10}
\]

is strict-upper complete in `J(4,2)`, but coordinate `3` has one internal
run of length two.  Hence no depth-two nonzero source word realizes it.
Owner Hamiltonicity plus upper chronology is not sufficient.

## 4. The collars force a staircase socket

Put

\[
 B_L=K\cup\{a_1,a_3,p_L\},\qquad
 u_0=\ell,qquad u_s=c_{\sigma(s)}\ (1\le s<d).        \tag{4.1}
\]

Let `P_s` be the union of the first `s` middle source cells after the left
collar.  The successive mixed owners are

\[
 V_0=B_L\cup C\cup\{\ell\},
\]

and

\[
 V_s=B_L\cup(C\setminus\{u_1,\ldots,u_{s-1}\})\cup P_s
       \qquad(1\le s\le d).                            \tag{4.2}
\]

### Theorem 4.1 (forced Johnson ladder and socket)

If `V_0,...,V_d` are distinct rank-`r` owners, then there are fresh labels
`y_1,...,y_d` such that

\[
                       V_s=V_{s-1}-u_{s-1}+y_s.        \tag{4.3}
\]

At `V_d`, coordinate `y_s` has occurred for exactly `d-s+1` owners.
Clipped residence therefore forces it to remain through at least the next
`s` owners.  The left collar exports the nested socket of depths

\[
                              1,2,\ldots,d.            \tag{4.4}
\]

The right collar imports the reversed socket.

#### Proof

The fixed part of `V_s` has size `r-s`.  Hence `P_s` supplies exactly `s`
coordinates outside it.  The `s-1` previously fresh labels remain because
the `P_s` are nested.  Reintroducing the outgoing label `u_(s-1)` without a
fresh label would repeat `V_(s-1)`; reintroducing it together with a fresh
label would give rank `r+1`.  Thus exactly one new `y_s` enters and (4.3)
holds.

The trace of `y_s` from `V_s` through `V_d` has current length `d-s+1`.
If it later becomes internal, residence requires `s` further occurrences.
This proves (4.4).  Reversal gives the right statement. \(\square\)

This is more than an endpoint-owner constraint: it is a literal `d`-step
source-history/cocycle constraint.

## 5. Exact overlap with the resident pivot/J6 path

Use the shared-bank notation of
`MATH_THEOREM_SHARED_BANK_PIVOT_RESIDENT_CYCLE_20260801.md`, with `h=d`.
Set

\[
\begin{aligned}
 B&=K\cup\{a_1,a_3,z\},&x_L&=a_3,&x_R&=z,\\
 D_i&=c_{\sigma(i)},&p&=p_L,&\rho_d&=\ell.
\end{aligned}                                                \tag{5.1}
\]

Then the pivot core is \(B\setminus\{x_L,x_R\}=K\cup\{a_1\}\), and its closing owner
is

\[
\begin{split}
 H&=(B\setminus\{z\})\cup\{p_L\}\cup C\cup\{\ell\}\\
  &=K\cup\{a_1,a_3,p_L\}\cup C\cup\{\ell\}=V_0.    \tag{5.2}
\end{split}
\]

### Theorem 5.1 (left collar--J6 overlap)

The final `d+1` source cells of the left collar,

\[
 \ell,c_{\sigma(1)},\ldots,c_{\sigma(d-2)},J_L^\sigma,Q_L, \tag{5.3}
\]

are an alternative inverse block for the J6 start owner `H`.  Append

\[
 U_i=(B\setminus\{z\})\cup\{\lambda_i\}
            \qquad(1\le i\le d),                     \tag{5.4}
\]

followed by the pivot letter, the `rho` bank, the closing source cell and
the first `d-1` cyclic source cells.  The resulting owner suffix is exactly
the opened J6 path

\[
 H,L_0,\ldots,L_{d-1},M_0,\ldots,M_d,R_0,\ldots,R_{d-1}. \tag{5.5}
\]

There is no owner duplication at the overlap.  The left residence debt is
paid exactly, and every cross-edge lower colour is literal.

#### Proof

Equation (5.2) proves the shared owner.  Each shift through (5.4) deletes,
in order,

\[
          \ell,c_{\sigma(1)},\ldots,c_{\sigma(d-1)}
\]

and inserts `lambda_1,...,lambda_d`, hence produces
`L_0,...,L_(d-1)`.  The remaining source cells are the explicit J6 inverse
and therefore give (5.5).

Coordinate `ell=rho_d` has a left-collar run of length `d+1`.  Coordinate
`c_(sigma(i))` has left suffix length `d-i+1` and J6 prefix length `i+1`;
the shared owner is counted twice, so its combined run has length

\[
                (d-i+1)+(i+1)-1=d+1.                  \tag{5.6}
\]

The shared source blocks in (5.3)--(5.4) contain every common endpoint
intersection, proving literal lower `q1`. \(\square\)

This overlap is a one-sided socket construction, not the common middle.
J6 is a balanced relay: its opposite end still exports the staircase
`1,...,d`, and it proves no consecutive-block upper surjectivity.

### 5.1 Exact `k=17` calibration

Take

\[
\begin{aligned}
K&=\{3,4,5\},&a_3&=0,&z&=1,&a_1&=2,\\
C&=(13,14),&\ell&=11,&p_L&=12,\\
(f_1,f_2,f_3)&=(7,6,8),&\rho&=9,&p_R&=10.
\end{aligned}                                                \tag{5.7}
\]

The filler transposition `f_1=7,f_2=6` avoids the one upper-colour collision
that occurs with the unmodified order `6,7,8`.  The full left collar is

```text
187 64 2237 2048 8192 16445 4157
```

and the appended J6 continuation is

```text
125 189 317 3 574 1086 2110 6204 12348 20540.
```

Its depth-three row has fourteen distinct rank-nine owners.  Starting at
offset three it is exactly the authenticated J6 order

```text
30781 28797 20733 4605 511 959
1855 3647 7742 15422 30782.
```

All thirteen lower and all thirteen upper edge colours of the combined
left-collar/J6 path are literal and distinct, and it has no wholly internal
positive run below four.

The tiny replay was compiled and run on one H100 CPU with a 256 MiB virtual
memory cap.  It reports

```text
PASS_K_CLIPPED_COMPARATOR_J6_LEFT_OVERLAP
owners=14
lower_q1_distinct=13
upper_q1_distinct=13
internal_short_runs=0.
```

### Proposition 5.2 (direct right return is rank-infeasible)

For the same `k=17` identification, the final J6 source history is

```text
2110 6204 12348 20540
```

and the first right-collar cell is `Q_R=1085`.  The next owner would be

\[
 6204\cup12348\cup20540\cup1085=31805,                 \tag{5.8}
\]

which has rank ten.  Equivalently it is

\[
                30782-\{z\}+\{a_3,p_R\}.              \tag{5.9}
\]

Therefore direct `J6 || R` concatenation cannot be the required rank-nine
owner chronology.

The same obstruction is structural under (5.1).  The terminal J6 owner is

\[
 R_{d-1}=(B\setminus\{a_3\})\cup\{p_L,\rho_d\}\cup D.
\]

Its outgoing source cell carries the unique `z`; after it leaves, `Q_R`
adds the two absent labels `a_3,p_R`.  The next window has rank `r+1`.
Thus a source-history rethread must install one of these labels while
removing another before the right collar can begin. \(\square\)

At `k=17` the J6 cut also removes upper colour `30783`; its old provider
`1484:6` must remain protected.  The overlap does not eliminate the frozen
extraction casualties, cover ranks above ten, or solve common cap.

## 6. Exact remaining theorem

The corrected global gate is the following.

> **Boundary chronology completion `BCC(k)`.**  Find a permutation `T` of
> all rank-`r` owners which extends the two fixed collar ladders, satisfies
> (3.4)--(3.6), has clipped `d`-resident coordinate traces, and is
> consecutive-block-union-surjective for every strict-upper target.  Inside
> the resulting nonempty caps choose one terminal common source and a
> distinct short-interval matching for all but `O(1)` strict-lower targets.

Theorem 3.1 constructs `M` once the owner order is given.  Theorem 2.1 makes
upper completeness an owner-order property.  Theorem 4.1 identifies the
two forced staircase sockets.  Theorem 5.1 shows that the resident J6 state
is an exact one-sided realization of one socket, while Proposition 5.2
proves that its frozen history cannot be returned directly into the other
collar.

Thus the present advance is not a proof of `BCC(k)`.  It replaces the broad
request for an arbitrary common middle word by one exact owner-order/cap
problem and supplies one authenticated left boundary buffer.  The open
piece is a protected upper-complete chronology which rethreads the outgoing
J6 history into the right collar and retains a bounded-defect terminal lower
matching.

## 7. Frozen dependencies and audit artifacts

```text
MATH_THEOREM_SHARED_BANK_PIVOT_RESIDENT_CYCLE_20260801.md
  963325b61c8af32df1c4395436ffa9b3fcea9d85890ae26e45098bb66a246fb3

MATH_THEOREM_SHARED_BANK_CYCLIC_RESERVOIR_AVOIDANCE_AND_SPLICE_GATE_20260801.md
  349b718a1b38ee33aa5389dd35121e91cc36a7e365059c621fbc5755f7116e87

MATH_THEOREM_THREAD_D_BOUNDARY_COATOM_RAIL_COMMONQ_MAXIMAL_EROSION_20260801.md
  5ca75f1d36f395556d8a81b92072e870f9cad46dd0632727b861819491ca859a

scratch/k17_compressed_pivot_path_j6_20260801.tsv
  34db7fc8fe70c59b98fb08b57c8a8f9c2bbe3bc2ed7f11bcfd33ad139528eeec

scratch/audit_k_clipped_comparator_j6_overlap_20260801.cpp
  06213d5c6dbea6303f6b77425d5ff7d7bdfa94a8aa2b5667ca33cfddf4302c55

scratch/k_clipped_comparator_j6_overlap_20260801.audit.json
  cf9d38b131dc4d3024283f11ad501868b7f35acef8b6f488171e544391e82294
```

The finite replay is a check of the `k=17` specialization only.  The
all-`d` statements above have symbolic proofs and do not rely on it.
