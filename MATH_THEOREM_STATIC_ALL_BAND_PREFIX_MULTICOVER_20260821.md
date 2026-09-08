# A static family of `W` permutation states covers every band rank

**Status (2026-08-21).**  This note proves an exact static counterpart of
the simultaneous union-coverage gate.  For odd `n=2m+1`, there are exactly

\[
 W={n\choose m}={n\choose m+1}
\]

permutation states whose unordered prefixes cover every target at every
rank.  The two middle layers are covered exactly once.  Thus there is no
set-theoretic incompatibility between the rankwise union requirements.

This is **not** a DCC construction.  The theorem says nothing about placing
the selected permutation states in one short tail-MTF/FIFO chronology.
Serializing arbitrary states separately would cost far too much.  The
remaining issue is therefore atomization/chronology, not the existence of a
simultaneously covering static state ensemble.

## 1. Statement

Let `n=2m+1`, let `[n]={1,...,n}`, and let

\[
 \mathcal L_k={ [n]\choose k},\qquad
 W=|\mathcal L_m|=|\mathcal L_{m+1}|.              \tag{1.1}
\]

For a permutation state `pi=(pi_1,...,pi_n)`, write

\[
 C_k(\pi)=\{\pi_1,\ldots,\pi_k\}.                 \tag{1.2}
\]

### Theorem 1.1 (exact static all-rank prefix multicover)

There is a family of permutation states

\[
 \{\pi_U:U\in\mathcal L_m\}                       \tag{1.3}
\]

such that, for every `0<=k<=n`,

\[
 \{C_k(\pi_U):U\in\mathcal L_m\}=\mathcal L_k.   \tag{1.4}
\]

The equality in (1.4) is equality of supports; repetitions are allowed.
At the two middle ranks there are no repetitions:

\[
 C_m(\pi_U)=U,qquad
 U\longmapsto C_{m+1}(\pi_U)
 \text{ is a bijection }\mathcal L_m\to\mathcal L_{m+1}. \tag{1.5}
\]

Consequently the same family simultaneously covers every prescribed band
`K subseteq {0,...,n}`.  At rank `k`, its `W` prefix occurrences have union
size exactly `binom(n,k)`, so the quota-relative union deficit is zero and
the only repeated mass is the unavoidable baseline
`W-binom(n,k)`.

## 2. The middle bijection

Join `U in L_m` to `V in L_(m+1)` when `U subset V`.  Every vertex on both
sides has degree `m+1`: an `m`-set has `m+1` one-element extensions, and an
`(m+1)`-set has `m+1` one-element deletions.  A regular bipartite graph with
equal shores has a perfect matching.  Fix one and denote it by

\[
 \Phi:\mathcal L_m\longrightarrow\mathcal L_{m+1},
 \qquad U\subset\Phi(U).                           \tag{2.1}
\]

We regard the `W` labels `U in L_m` as distinguishable tokens.  Initially
token `U` occupies `U` at level `m` and `Phi(U)` at level `m+1`.

## 3. Sending the tokens down while covering every set

Suppose `1<=k<=m` and that the `W` tokens occupy members of `L_k`, with
every member of `L_k` occupied at least once.  Replace each occupied set by
as many distinguishable copies as there are tokens on it.  We claim that
the tokens can be sent to contained `(k-1)`-sets so that every member of
`L_(k-1)` receives a token.

Indeed, let `T subseteq L_(k-1)` and let `Gamma(T) subseteq L_k` be its
upper shadow.  Count containment incidences.  Every member of `T` has
`n-k+1` one-element extensions, whereas a member of `Gamma(T)` contains at
most `k` members of `T`.  Hence

\[
 |\Gamma(T)|\ge {n-k+1\over k}|T|\ge |T|,          \tag{3.1}
\]

where the last inequality uses `k<=m` and `n=2m+1`.  Since every set in
`Gamma(T)` has at least one token-copy, the neighborhood of `T` in the
copy-expanded containment graph has size at least `|T|`.  Hall's theorem
therefore matches every `(k-1)`-set to a distinct token-copy on a containing
`k`-set.  Send those matched tokens to their matched sets, and send every
unmatched token to an arbitrary contained `(k-1)`-set.

This preserves all `W` token labels and makes every member of `L_(k-1)`
nonempty.  Iterating from `k=m` down to `1` gives, for every token `U`, a
nested lower chain

\[
 S_0(U)\subset S_1(U)\subset\cdots\subset S_m(U)=U,
 \qquad |S_k(U)|=k,                                \tag{3.2}
\]

whose support at level `k` is all of `L_k`.

## 4. Sending the tokens up while covering every set

The upper induction is symmetric.  Suppose `m+1<=k<n` and the `W` tokens
occupy `L_k`, every member at least once.  For `T subseteq L_(k+1)`, let
`partial(T) subseteq L_k` be its lower shadow.  Each member of `T` has
`k+1` one-element deletions, while a member of `partial(T)` is contained in
at most `n-k` members of `T`.  Thus

\[
 |\partial(T)|\ge {k+1\over n-k}|T|\ge |T|,        \tag{4.1}
\]

because `k>=m+1`.  Hall's theorem in the copy-expanded containment graph
matches every `(k+1)`-set to a distinct token-copy on one of its `k`-set
subsets.  Send the remaining copies arbitrarily upward.

Starting from the bijective occupation `Phi(U)` of `L_(m+1)` and iterating
to level `n` gives nested upper chains

\[
 \Phi(U)=S_{m+1}(U)\subset S_{m+2}(U)\subset\cdots
 \subset S_n(U)=[n],
 \qquad |S_k(U)|=k,                                \tag{4.2}
\]

with full support at every level.

## 5. Realization by permutation states

For each token `U`, equations (2.1), (3.2), and (4.2) form a maximal chain

\[
 \varnothing=S_0(U)\subset S_1(U)\subset\cdots
 \subset S_n(U)=[n],qquad |S_k(U)|=k.             \tag{5.1}
\]

There is a unique permutation `pi_U` whose `k`th entry is the unique element
of `S_k(U)\setminus S_(k-1)(U)`.  Then

\[
 C_k(\pi_U)=S_k(U)                                 \tag{5.2}
\]

for every `k`.  Full support at every level proves (1.4), and the fixed
middle matching proves (1.5).  This completes the proof of Theorem 1.1.

## 6. Exact scope

The theorem removes three possible static obstructions at once:

1. all ranks can be covered by one common family of full states;
2. the two middle ranks can simultaneously be collision-free; and
3. upper and lower prefix chains can be chosen coherently inside each state.

It does not control the distance between different `pi_U`, the generator
word joining them, repeated observations along such joins, or the number of
FIFO atoms needed to realize the family.  Any use in a coefficient-one DCC
proof therefore still needs a decomposition of almost all these states into
`o(W)` physically serializable atoms, or a different chronology that realizes
the same union support with only `o(W)` transition overhead.
