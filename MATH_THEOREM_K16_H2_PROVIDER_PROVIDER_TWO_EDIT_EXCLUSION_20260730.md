# K16 H2 provider/provider exclusion: simultaneous interval normal form and the 280,030,360-to-12-to-zero atlas

Date: 2026-07-30  
Lane: K  
Status: the final two-substitution face of the frozen H2 word is exactly closed

## 1. Result

Let $W$ be the frozen length-$12873$ word

    scratch/k16_ejection_lns_h2_p110_20260730.word

with SHA-256

    5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7

and exact holes

\[
A=0x4879\subset B=0x6879.
\tag{1.1}
\]

The earlier theorems closed:

1. every two-edit pair whose two endpoint values are source non-providers;
2. every mixed source-nonprovider/source-provider pair; and
3. every provider-first intermediate having at most seven holes.

This note closes the only remaining face.

> **Provider/provider exclusion theorem.**  There is no universal word
> obtained from $W$ by changing two distinct positions to values which are
> each source providers for $A$ or $B$.

Consequently no universal word is obtainable from $W$ by at most two
substitutions. This is a theorem about this frozen word, not a K16 lower
bound: three or more substitutions, insertions/deletions, other words, and
the separate H1 radius-three lane remain outside the claim.

## 2. One-position residuals and source-provider domains

For a word $V$, target $T$ and position $p$, extend left and right from $p$
through the maximal consecutive fixed letters which are submasks of $T$.
Let $c_p^V(T)$ be their OR and put

\[
r_p^V(T)=T\setminus c_p^V(T).
\tag{2.1}
\]

Replacing $p$ by $x$ creates a $p$-containing $T$-witness exactly when

\[
r_p^V(T)\subseteq x\subseteq T.
\tag{2.2}
\]

Indeed the full maximal compatible interval works when (2.2) holds, and
every $p$-containing $T$-interval is contained in it.

For a source hole $H\in\{A,B\}$ define the exact source-provider domain

\[
\Pi_p(H)=
[r_p^W(H),H]\setminus\{0\}.
\tag{2.3}
\]

Because $H$ is missing from $W$, the incumbent $w_p$ is not in $\Pi_p(H)$.
Thus a source-provider edit at $p$ has value in
$\Pi_p(A)\cup\Pi_p(B)$, and literal change is automatic.

## 3. Symmetric simultaneous two-provider normal form

Fix distinct positions $p<q$ and let $S=\{p,q\}$. A covered target $T$ is
**pair-exclusive** if every old $T$-witness meets $S$. Equivalently, if
$N_T,N_T(p),N_T(q),N_T(p,q)$ count all old witnesses, those meeting $p$,
those meeting $q$, and those meeting both, then

\[
N_T=N_T(p)+N_T(q)-N_T(p,q).
\tag{3.1}
\]

Treat the other edited position as a blocker and take the maximal
$T$-compatible fixed context for a witness containing $p$ but not $q$.
Call its residual $r_{p\mid\bar q}(T)$; define
$r_{q\mid\bar p}(T)$ symmetrically. A witness containing both positions is
possible only if every fixed bridge letter $w_{p+1},\ldots,w_{q-1}$ is a
submask of $T$. When this bridge condition holds, extend through the maximal
compatible exterior context and call the remaining residual $r_{pq}(T)$.

After the replacements $p\leftarrow x,q\leftarrow y$, every source hole and
every pair-exclusive covered target $T$ is covered exactly when at least one
of the following three forms holds:

\[
\begin{aligned}
&r_{p\mid\bar q}(T)\subseteq x\subseteq T,\tag{3.2a}\\
{}\lor{}\;&r_{q\mid\bar p}(T)\subseteq y\subseteq T,\tag{3.2b}\\
{}\lor{}\;&\bigl[
  \text{the fixed bridge is contained in }T,
  \quad x,y\subseteq T,
  \quad r_{pq}(T)\subseteq x\vee y
\bigr].\tag{3.2c}
\end{aligned}
\]

Every final witness meeting $S$ has exactly one of these support types, and
the maximal context of that type supplies a witness whenever its displayed
condition holds. Targets having an old witness avoiding $S$ impose no row.
Therefore (3.2), together with

\[
x\in\Pi_p(A)\cup\Pi_p(B),\qquad
y\in\Pi_q(A)\cup\Pi_q(B),
\tag{3.3}
\]

is an exact simultaneous occurrence-level normal form for the
provider/provider face. It retains common witnesses and all exclusive
covered targets; it is not a marginal or hole-count relaxation.

## 4. Canonical orientation and the two Boolean role rows

The symmetric form has a sharper oriented quotient. In any completed word,
a final $A$-witness uses at least one edited position because $A$ is missing
from $W$. Choose such an endpoint as $q$. Its new literal lies in that
witness, hence

\[
y\subseteq A.
\tag{4.1}
\]

On the provider/provider face this $q\leftarrow y$ is a source-provider move.
Put

\[
V=W^{q\leftarrow y},\qquad
\mathcal H(V)=\operatorname{holes}(V),\qquad
I(V)=\bigcap_{T\in\mathcal H(V)}T.
\tag{4.2}
\]

The authenticated provider-first theorem already excludes
$|\mathcal H(V)|\le7$, so only high states need be retained.

For a possible second position $p\ne q$, define the hole requirement

\[
R_p(V)=\bigvee_{T\in\mathcal H(V)}r_p^V(T).
\tag{4.3}
\]

Every current hole must be created through $p$, so the exact hole-only domain
is

\[
[R_p(V),I(V)]\setminus\{0\}.
\tag{4.4}
\]

Let $\mathcal E_p(V)$ be the covered targets all of whose $V$-witnesses use
$p$, and put

\[
L_p(V)=R_p(V)\vee
       \bigvee_{T\in\mathcal E_p(V)}r_p^V(T),
\qquad
U_p(V)=I(V)\cap
       \bigcap_{T\in\mathcal E_p(V)}T.
\tag{4.5}
\]

Then the exact one-cell completion values of $V$ at $p$ are the nonzero part
of $[L_p(V),U_p(V)]$. Intersecting this with one source-provider role
$H\in\{A,B\}$ gives one Boolean interval:

\[
\boxed{
\mathcal C^H_{p;q,y}
=
[L_p(V)\vee r_p^W(H),\ U_p(V)\cap H]\setminus\{0,w_p\}.
}
\tag{4.6}
\]

Thus every oriented state/position row has only the two roles $A,B$; there
is no value scan. A row is feasible exactly when its lower endpoint is a
submask of its upper endpoint and its upper endpoint is nonzero. The
incumbent exclusion is automatic within a source-hole provider role. Before
computing covered exclusive targets, the necessary hole-stage role interval
is

\[
\mathcal C^{H,0}_{p;q,y}
=
[R_p(V)\vee r_p^W(H),\ I(V)\cap H]\setminus\{0\}.
\tag{4.7}
\]

Any bit in the lower endpoint but not the upper endpoint is an explicit
forcing/forbidding certificate. Covered $p$-exclusive targets only strengthen
(4.7).

There is also a symmetric mutual-anchor consequence. If high source-provider
moves $a,b$ complete one another and $I_a$ is the intersection of the holes
after $a$, then

\[
\operatorname{value}(a)\subseteq I_b,
\qquad
\operatorname{value}(b)\subseteq I_a.
\tag{4.8}
\]

The frozen intersections have at most six bits, so even a direct mutual
anchor join needs at most $64$ submasks per state rather than a quadratic
join. The stronger interval census below already dies before that join is
needed.

## 5. Exact frozen census

The source-provider enumeration partitions as

\[
44421=284+44137,
\tag{5.1}
\]

where the $284$ low states are frozen by the earlier theorem. The high states
partition as

\[
44137=805+43332,
\tag{5.2}
\]

where $805$ already have $I(V)=0$. Among the $43332$ nonzero-intersection
states, the canonical orientation (4.1) gives

\[
43332=21577+21755.
\tag{5.3}
\]

The $21755$ retained states and all $12872$ possible second positions give

\[
21755\cdot12872=280030360
\tag{5.4}
\]

state/position rows.

### 5.1 Generic current-hole contradiction

Exactly

\[
280030348
\tag{5.5}
\]

rows satisfy

\[
R_p(V)\nsubseteq I(V).
\tag{5.6}
\]

For each such row, a bit in $R_p(V)\setminus I(V)$ is forced by the maximal
context of some current hole but omitted by another current hole. Therefore
no single second value exists, provider or otherwise. The primary audit
stores the complete deterministic least-killer-bit histogram.

### 5.2 The twelve survivors and the source-provider contradiction

Only twelve rows satisfy $R_p(V)\subseteq I(V)$. In every one,

\[
y=A,\qquad q-p=6438.
\tag{5.7}
\]

Their exact hole-stage data are:

| $q$ | $p$ | $R_p(V)$ | $I(V)$ | $r_p^W(A)\setminus I(V)$ | $r_p^W(B)\setminus I(V)$ |
|---:|---:|---:|---:|---:|---:|
| 7650 | 1212 | 0x8838 | 0x8838 | 0x0040 | 0x0040 |
| 7652 | 1214 | 0xa409 | 0xa409 | 0x4870 | 0x0040 |
| 7818 | 1380 | 0x8900 | 0xe908 | 0x0071 | 0x0051 |
| 7820 | 1382 | 0xa888 | 0xa888 | 0x4071 | 0x0051 |
| 8685 | 2247 | 0xa08a | 0xa08a | 0x4871 | 0x4871 |
| 8687 | 2249 | 0xe802 | 0xe802 | 0x0079 | 0x0079 |
| 9288 | 2850 | 0xa8c8 | 0xa8c8 | 0x4031 | 0x4011 |
| 9290 | 2852 | 0xa8c4 | 0xa8c4 | 0x4039 | 0x4019 |
| 9304 | 2866 | 0xa644 | 0xa644 | 0x4839 | 0x4839 |
| 9306 | 2868 | 0xa214 | 0xa234 | 0x4849 | 0x4849 |
| 10133 | 3695 | 0xa0b8 | 0xa0b8 | 0x4841 | 0x4041 |
| 10135 | 3697 | 0x8120 | 0x8938 | 0x4041 | 0x4041 |

Every entry in each of the last two columns is nonzero. An $H$-provider must
contain $r_p^W(H)$, while every value covering all current holes must be a
submask of $I(V)$. These requirements conflict for both $H=A$ and $H=B$ in
all twelve rows. Hence

\[
12\longrightarrow0
\tag{5.8}
\]

before any covered exclusive-target constraint is used. In the audit's
residual-first mutually exclusive classification, all twelve $A$ rows and all
twelve $B$ rows are assigned to residual kills, so no row reaches the later
bound-kill branch. There are zero candidate role rows and zero candidate
values.

The provider/provider and mixed faces therefore complement one another on
the same twelve geometric rows: provider values fail already at the source
residual/current-hole interface, while the earlier mixed audit needed one
covered exclusive target to kill the surviving non-provider values.

## 6. Independent audit and authentication

The independent verifier literally reconstructs each of the twelve
intermediate words, enumerates all interval-OR multiplicities, recomputes its
complete hole family and the interval $[R_p(V),I(V)]$, and independently
enumerates every source $A$-provider and $B$-provider value at $p$. It finds
zero provider values in the hole interval for every row.

The global $280030360\to12$ enumeration is source-audited and cross-checked
against the earlier frozen provider and mixed atlases; the independent
Python verifier does not re-enumerate all $280$ million rows. Its exact scope
is recorded in the artifact.

Primary hashes:

    primary C++ source
      4b24c59e29dbe0d4344a047390e3e95a11bc0dd710254ea48dc77ec52cc43ee6
    Linux binary
      9d2c44604765b9d63a529f67d4ffdd18f1f97af19027b2187e860eaf3d05c174
    primary audit
      e7c9b2dc98a606ab0000acfd8a575da9bd7a6fb837e3f94130461fe490cf56c9
    independent source
      c5238792278e5d3fcdf42cde655a8546086e50ecc6927cbc45cd5d8bb53d98a6
    independent audit
      c958bf2f7fb0d6a779bb11b92d2b296b237e46ab7dd126eaeb4fdca35887d829
      payload 2deedaa7722ab69561693f1abfcae5a2f02c47039e702df1ed7b8f39deb79574
      rows payload b2239e9fc24054af1c02f87c237e92a7ada9b6c6a4ca0e04238ecc5d67ae08ec
    package manifest
      9b4e630ec991b71ad28f0e1f56b0499c5b8f17d3701a71cf72ec46d5bdc53f20
      payload 34880bb36eccccab30f66ba73bc07f28f7db680bd277f79b07f51a67c443b21b

All remote work used one H100 CPU under

    /home/amodo/or15/work/laneK_h2_provider_provider_20260730

with no `/dev/shm` write. Compilation and enumeration had $512$ MiB address
caps; the independent replay had a $256$ MiB cap; every stage had a
$120$-second timeout. The authenticated enumeration rerun took $8.60$ seconds
with $12800$ KiB maximum RSS, and the independent replay took $0.77$ seconds
with $103108$ KiB maximum RSS. Every retained authenticated stage exited
zero. Timeout, ENOSPC, signal, or nonzero exit of a theorem-producing run
was designated UNKNOWN.

## 7. Sharp final scope

For the frozen H2 word:

- both source-nonprovider endpoints are excluded by the earlier exact
  two-cell form theorem;
- the mixed face is excluded by the occurrence-core/exclusive-supply theorem;
- low provider-first states are excluded by the authenticated floor-eight
  sweep; and
- the remaining high provider/provider face is excluded here.

Support zero fails because $W$ has the holes $A,B$. Any support-one
completion would necessarily be a source provider; the complete frozen
provider after-state histogram has hole counts from $1$ through $21$ and no
zero-hole state. Hence support one also fails. Together with the exhaustive
two-endpoint partition above, support at most two is completely closed for
substitutions of this word. The exact K16 bracket is unchanged. The separate
H1 radius-three lane and every architecture using three or more lasting edits
remain live and are not constrained by this theorem.
