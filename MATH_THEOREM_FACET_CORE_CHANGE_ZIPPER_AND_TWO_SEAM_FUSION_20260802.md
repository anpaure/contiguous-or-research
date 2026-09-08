# Core-change zipper and two-seam fusion for unbuffered alternating cycles

Date: 2026-08-02  
Status: unconditional local source/owner/immediate-palette theorem.  It
connects two already constructed alternating source cycles while preserving
owner simplicity, both immediate-palette simplicities, and the owner
residence floor.  It does **not** preserve the literal names of the removed
owners, prove any deeper upper palette, bind compiler cells, or produce a
complete universal word.

## 0. Parameters and outcome

Let

\[
 h=q-1=d+1\ge2
\]

be the owner-window length.  Let

\[
 X=C\dot\cup\{a\},\qquad Y=C\dot\cup\{b\},
 \qquad |C|=r-h-2,                                      \tag{0.1}
\]

where `a`, `b`, and the refreshed point `beta` are distinct and outside
`C`.  Thus

\[
 |X|=|Y|=r-h-1=r-q.                                    \tag{0.2}
\]

For a private tag `z`, write

\[
 P_X(z)=X\cup\{z\},\qquad H_X(z)=X\cup\{\beta,z\},     \tag{0.3}
\]

and define `P_Y,H_Y` analogously.  Sources alternate strictly between `P`
and `H`.

The theorem below gives a literal zipper between the adjacent cores `X`
and `Y`.  The repeated tag on the two source letters at the seam pays
exactly for the extra core point:

\[
 \underbrace{|X\cup Y|-|X|}_{+1\text{ core}}
 +
 \underbrace{(h-1)-h}_{-1\text{ tag}}=0.               \tag{0.4}
\]

Consequently all mixed `h`-windows remain rank `r`, and the affected owner
row is a Johnson geodesic.  Two such zippers fuse two cyclic components.

## 1. One zipper

Consider a cut with the following tag halo.  The last `h` sources on the
`X` side have tags

\[
 \ell _0,\ell _1,\ldots,\ell _{h-2},z,                 \tag{1.1}
\]

and the first `h` sources on the `Y` side have tags

\[
 z,\rho _1,\rho _2,\ldots,\rho _{h-1}.                 \tag{1.2}
\]

Assume:

1. all symbols displayed in (1.1)--(1.2), other than the two displayed
   occurrences of `z`, are pairwise distinct;
2. all tags are disjoint from `C union {a,b,beta}`;
3. the two sources carrying `z` have opposite `P/H` types, and each side
   continues the strict alternation away from the cut.

Condition 1 is a convenient strong zipper condition.  The exact weaker
condition is that, for every `1<=t<h`,

\[
 \{\ell_t,\ldots,\ell_{h-2}\}
 \cap\{\rho_1,\ldots,\rho_{t-1}\}=\varnothing.          \tag{1.3}
\]

The strong form is what is used in the two-cycle corollary.

Let `O_t`, `0<=t<=h`, be the successive length-`h` owner windows, from the
last pure `X` owner through the first pure `Y` owner.  Direct union gives

\[
\begin{aligned}
 O_0={}&C\cup\{a,\beta\}
       \cup\{\ell_0,\ldots,\ell_{h-2},z\},\\
 O_t={}&C\cup\{a,b,\beta\}
       \cup\{\ell_t,\ldots,\ell_{h-2},z,
                       \rho_1,\ldots,\rho_{t-1}\},
                       &&1\le t<h,\\
 O_h={}&C\cup\{b,\beta\}
       \cup\{z,\rho_1,\ldots,\rho_{h-1}\}.
                                                               \tag{1.4}
\end{aligned}
\]

Every mixed window contains both boundary sources.  It therefore contains
both core points `a,b`, the common refreshed point `beta`, and exactly
`h-1=q-2` distinct tags: `z` is counted once although it occurs in two
sources.  Hence

\[
 |O_t|=(r-h-2)+2+1+(h-1)=r\qquad(1\le t<h).             \tag{1.5}
\]

The endpoint calculation is the same:

\[
 |O_0|=|O_h|=(r-h-2)+1+1+h=r.                           \tag{1.6}
\]

### Theorem 1.1 (zipper geodesic)

The owner sequence in (1.4) is a simple Johnson path.  More precisely,

\[
\begin{array}{c|c|c}
\text{transition}&\text{deleted}&\text{inserted}\\ \hline
O_0\to O_1&\ell_0&b\\
O_t\to O_{t+1},\ 1\le t\le h-2&\ell_t&\rho_t\\
O_{h-1}\to O_h&a&\rho_{h-1}.
\end{array}                                             \tag{1.7}
\]

In particular, the first transition changes an old tag into the new core
point, the interior transitions change tags, and the last transition
changes the old core point into a new tag.

#### Proof

Subtract consecutive formulas in (1.4).  Condition 1 and the disjointness
from the cores ensure that the deleted and inserted elements in every row
of (1.7) are different and that the inserted element was not already
present.  Thus every transition has symmetric difference two.  The mixed
owners all contain `a,b`, whereas the endpoints omit respectively `b,a`.
The mixed tag sets are strictly changed by the displayed `ell_t -> rho_t`
swaps, so no owner repeats.  \(\square\)

## 2. Exact immediate colours

Put

\[
 I_t=O_t\cap O_{t+1},\qquad U_t=O_t\cup O_{t+1}
 \qquad(0\le t<h).                                      \tag{2.1}
\]

The exact lower colours are

\[
\begin{aligned}
 I_0={}&C\cup\{a,\beta\}
        \cup\{\ell_1,\ldots,\ell_{h-2},z\},\\
 I_t={}&C\cup\{a,b,\beta\}
        \cup\{\ell_{t+1},\ldots,\ell_{h-2},z,
                         \rho_1,\ldots,\rho_{t-1}\},
                         &&1\le t\le h-2,\\
 I_{h-1}={}&C\cup\{b,\beta\}
        \cup\{z,\rho_1,\ldots,\rho_{h-2}\},          \tag{2.2}
\end{aligned}
\]

and the exact upper colours are

\[
\begin{aligned}
 U_0={}&C\cup\{a,b,\beta\}
        \cup\{\ell_0,\ldots,\ell_{h-2},z\},\\
 U_t={}&C\cup\{a,b,\beta\}
        \cup\{\ell_t,\ldots,\ell_{h-2},z,
                         \rho_1,\ldots,\rho_t\},
                         &&1\le t\le h-2,\\
 U_{h-1}={}&C\cup\{a,b,\beta\}
        \cup\{z,\rho_1,\ldots,\rho_{h-1}\}.          \tag{2.3}
\end{aligned}
\]

Empty ranges in these formulas are omitted.  Therefore

\[
 |I_t|=r-1,qquad |U_t|=r+1.                             \tag{2.4}
\]

### Proposition 2.1 (one-seam palette simplicity)

The `h` lower colours in (2.2) are pairwise distinct, and the `h` upper
colours in (2.3) are pairwise distinct.

#### Proof

The two endpoint lower colours contain respectively `a` but not `b`, and
`b` but not `a`; every interior lower colour contains both.  Two interior
indices are separated by the first `ell` deleted, equivalently by the first
`rho` inserted.  This proves lower injectivity.

All upper colours have common fixed part `C union {a,b,beta}`.  Their tag
sets form the simple geodesic

\[
 \{\ell_0,\ldots,\ell_{h-2},z\}
 \longrightarrow\cdots\longrightarrow
 \{z,\rho_1,\ldots,\rho_{h-1}\},                       \tag{2.5}
\]

with one `ell_t -> rho_t` exchange at each step.  The tag sets, and hence
the upper colours, are distinct.  \(\square\)

## 3. Two-seam fusion

Let `A` and `B` be two directed cyclic source words of even lengths
`L_A,L_B>=h+2`.  Word `A` uses core `X`, word `B` uses core `Y`; both use
the same refreshed point `beta`.  Each word alternates `P,H` strictly and
has a tag sequence with no repetition.

Cut the directed edges

\[
 A_{L_A-1}\longrightarrow A_0,
 \qquad
 B_{L_B-1}\longrightarrow B_0.                          \tag{3.1}
\]

Assume the tag sequences satisfy

\[
 \operatorname{tag}(A_0)=w,quad
 \operatorname{tag}(A_{L_A-1})=z,quad
 \operatorname{tag}(B_0)=z,quad
 \operatorname{tag}(B_{L_B-1})=w,                       \tag{3.2}
\]

and that their two tag supports meet exactly in `{z,w}`.  All tags are
outside `C union {a,b,beta}`.

Finally require the two deleted edges to have the same ordered `P/H`
phase.  Equivalently,

\[
 \operatorname{type}(A_{L_A-1})
   =\operatorname{type}(B_{L_B-1}),qquad
 \operatorname{type}(A_0)=\operatorname{type}(B_0).     \tag{3.3}
\]

Delete (3.1) and insert

\[
 A_{L_A-1}\longrightarrow B_0,
 \qquad
 B_{L_B-1}\longrightarrow A_0.                          \tag{3.4}
\]

The result is the single directed source cycle

\[
 A_0,A_1,\ldots,A_{L_A-1},
 B_0,B_1,\ldots,B_{L_B-1}.                               \tag{3.5}
\]

Condition (3.3) is necessary and sufficient for (3.5) to remain strictly
alternating.  Since `L_A,L_B>=h+2`, the `z`-halo excludes `w`, and the
`w`-halo excludes `z`.  Thus both new seams satisfy the strong zipper
condition of Section 1.

### Theorem 3.1 (two-cycle fusion)

Assume each input cycle has simple rank-`r` owner, rank-`r-1` immediate
lower, and rank-`r+1` immediate upper palettes.  Under (0.1)--(0.3) and
(3.1)--(3.4), the fused cycle has:

1. exactly `L_A+L_B` distinct rank-`r` owners;
2. exactly `L_A+L_B` distinct rank-`r-1` immediate lower colours;
3. exactly `L_A+L_B` distinct rank-`r+1` immediate upper colours;
4. cyclic coordinate-residence floor at least `h`.

#### Proof: owner and upper palettes

Every retained pure `A` owner/upper colour contains `a` and not `b`; every
retained pure `B` owner/upper colour contains `b` and not `a`.  Every new
mixed owner and every new upper colour contains both.  Hence no mixed item
collides with a retained pure item, and the two pure decks cannot collide
with one another.

Within one seam, simplicity is Theorem 1.1 and Proposition 2.1.  Every
mixed tag set at the `z` seam contains `z` and excludes `w`, while every
mixed tag set at the `w` seam contains `w` and excludes `z`.  The two new
seam decks are therefore disjoint.  This proves owner and upper
simplicity.

#### Proof: lower palette

The interior new lower colours contain both `a,b`, so the preceding
argument handles them.  The endpoint lower colours contain only one of
`a,b`.  For core `X`, their tag parts are precisely

\[
 \{\operatorname{tag}(A_{L_A-h+1}),\ldots,
                    \operatorname{tag}(A_{L_A-1})\},
 \qquad
 \{\operatorname{tag}(A_0),\ldots,
                    \operatorname{tag}(A_{h-2})\}.       \tag{3.6}
\]

They are the two proper cyclic `(h-1)`-interval colours exposed at the
deleted cut.  They are distinct because `L_A>=h+2`, and the original
fixed-length cyclic intervals had distinct starts.  Their unique original
occurrences were among the transitions removed by the rethread, so neither
duplicates a retained pure lower colour.  The same argument applies to
`B`.  Different cores are separated by `a,b`, and the two seams are
separated by `z,w`.  Thus the complete lower palette is simple.

#### Proof: residence

Any owner is the union of `h` consecutive sources.  A single occurrence of
a coordinate in the source cycle therefore creates `h` consecutive owner
occurrences.  A union of such length-`h` cyclic intervals has no nonempty
connected component shorter than `h`.

Here the residence can be read exactly.  Every ordinary private tag occurs
in one source and has an owner run of length `h`.  Each seam tag `z,w`
occurs in two adjacent sources and has a run of length `h+1`.  The point
`beta` belongs to every owner because the fused source word alternates and
`h>=2`.  Every point of `C` belongs to every owner.  The points `a,b` have
runs of lengths `L_A+h-1` and `L_B+h-1`, respectively.  Because the
opposite block has length at least `h+2`, neither run wraps into itself.
Thus every coordinate run has length at least `h`.  \(\square\)

## 4. Application to the corrected unbuffered cycles

The corrected alternating cycles in
`MATH_THEOREM_FACET_UNBUFFERED_MULTIPRIMITIVE_CLUSTERED_PRUNING_AND_SOCKET_RESERVATION_20260802.md`
have

\[
 L=\begin{cases}q+1=h+2,&q\text{ odd},\\
                  q+2=h+3,&q\text{ even},
   \end{cases}                                           \tag{4.1}
\]

so the separation `L>=h+2` needed above is automatic.  If two extracted
cycles have adjacent cores `C+a,C+b`, a common `beta`, two cross-positioned
shared tags `z,w`, and same-phase cuts, Theorem 3.1 fuses them without an
owner/q1 collision or residence loss.

This is a genuine component-fusion rule, but it is conditional on finding
the two shared-tag sockets and adjacent cores inside the extracted bank.
The clustered-pruning theorem does not currently guarantee that socket
graph.  Moreover, fusion replaces the named owner and palette values in
the cut halos; simplicity is preserved, not the original literal deck.

## 5. Strict scope

This theorem proves only:

* literal source-cycle fusion;
* rank-`r` owner flatness and simplicity;
* rank-`r-1` and rank-`r+1` immediate-palette simplicity;
* positive coordinate residence at least `h=d+1`.

It does not prove:

* that the changed owner set is the complete middle layer;
* preservation or coverage of upper ranks `r+2,...,k`;
* preservation of the complete marked lower deck below q1;
* occurrence-position pins or a lower compiler/common cap;
* existence of enough socket-compatible pairs to connect all extracted
  cycles;
* regeneration of a second pure-core socket after using a shortest cycle's
  first socket (the shortest lengths are below `2h` for `h>=4`);
* an all-`k` universal word or any new value of `nu(k)`.
