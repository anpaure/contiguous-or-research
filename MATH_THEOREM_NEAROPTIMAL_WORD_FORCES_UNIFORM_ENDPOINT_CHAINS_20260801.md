# Near-optimal OR words force a uniform endpoint-chain decomposition

Date: 2026-08-01  
Status: unconditional necessary theorem for every universal word.  It is
independent of the flat-carrier, Johnson, Pascal and common-cap ansatzes.

## 1. Statement

Let `A=(A_1,...,A_L)` be a word of nonempty subsets of `[k]` whose
contiguous unions contain every nonempty subset of `[k]`.  Put

\[
 r=\lceil k/2\rceil,
 \qquad W={k\choose r},
 \qquad L=W+e.                                      \tag{1.1}
\]

Write

\[
 \mathcal L_{<r}=\{X\subseteq[k]:1\le |X|<r\}.
\]

### Theorem 1.1 (endpoint-chain theorem)

The lower ideal `L_<r` can be partitioned into at most `L` inclusion
chains, each of size at most `e`.  More precisely, the chain indexed by
right endpoint `j` has size at most `min(e,j)` (with one-based endpoints).

Consequently

\[
 |\mathcal L_{<r}|
   \le \sum_{j=1}^{L}\min(e,j)
   =eW+{e+1\choose2}.                               \tag{1.2}
\]

Thus this chain theorem recovers the sharp monotone-deadline lower bound
and gives additional structure behind it.

#### Proof

For every rank-`r` target `T`, choose one witnessing interval `I_T`.  Two
chosen intervals cannot contain one another: if `I_T subset I_T'`, then
`T subset T'`, and equal rank forces `T=T'`.  They are also distinct.

Order the `W` intervals by increasing left endpoint,

\[
                       I_i=[\ell_i,u_i]
                       \qquad(1\le i\le W).          \tag{1.3}
\]

Noncontainment makes both endpoint sequences strictly increasing.  Hence

\[
                       \ell_i\ge i,
 \qquad               u_i\le L-(W-i)=i+e,           \tag{1.4}
\]

and therefore

\[
                            I_i\subseteq[i,i+e].      \tag{1.5}
\]

Every interval of length at least `e+1` contains a chosen rank-`r`
interval.  Indeed, an interval of length exactly `e+1` has the form
`[a,a+e]` with `1<=a<=L-e=W`, and it contains `I_a` by (1.5); a longer
interval contains such a subinterval.  Its union consequently contains a
rank-`r` set and cannot represent a member of `L_<r`.

Choose one witnessing interval for every member of `L_<r`.  Every chosen
lower witness has length at most `e`.  Group these targets by the right
endpoint `j` of their chosen witness.  At fixed `j`, the possible witnesses
are

\[
 [j,j], [j-1,j],\ldots,[\max(1,j-e+1),j].            \tag{1.6}
\]

Their unions are nested by inclusion, so the targets assigned to endpoint
`j` form a chain.  There are at most `min(e,j)` such intervals.  The groups
partition the lower targets because one witness was selected per target.
Summing their capacities proves (1.2).  \(\square\)

## 2. Additive-constant consequence

Let

\[
 \Lambda=\sum_{t=1}^{r-1}{k\choose t},
 \qquad
 d(k)=\min\{d:dW+{d+1\choose2}\ge\Lambda\}.         \tag{2.1}
\]

If `nu(k)<=B(k)+C=W+d(k)+C`, then the whole lower ideal has a partition
into at most `W+d(k)+C` chains, each of length at most `d(k)+C`.
Since

\[
 {\Lambda\over W}=d(k)+O(1),
 \qquad d(k)=\sqrt{\pi k/8}+O(1),                    \tag{2.2}
\]

this is an asymptotically average-length, endpoint-serialized chain
decomposition of the lower half.

For even `k`, the relevant full-lattice average is

\[
 {2^k\over W}=\sqrt{\pi k/2}+O(k^{-1/2})
              =2d(k)+O(1).                          \tag{2.3}
\]

The reciprocal `W/2^k` is `Theta(k^(-1/2))` and must not be confused with
the chain length.  Complementing the lower chains gives the matching upper
scale, but pairing the two shores into symmetric serialized chains is an
additional problem, not a consequence of Theorem 1.1.

## 3. Interpretation

This theorem explains why an additive-constant result is not merely a
middle-layer Hamiltonicity statement.  A near-optimal word must serialize
the entire lower Boolean ideal into almost uniformly short suffix-OR chains.
An abstract uniform or symmetric chain decomposition is still insufficient:
the chains must arise from the common next-occurrence dynamics of one word.

Conversely, Theorem 1.1 is only necessary.  It does not construct one word,
couple the endpoint chains to the upper witnesses, or solve residence and
the common-cap realization.

## 4. Replay

Run

```text
python3 scratch/audit_uniform_endpoint_chain_interval_lemma_20260801.py
```

The replay exhausts every noncontaining interval family for `L<=9`, checks
(1.4)--(1.5), checks that every length-`e+1` interval contains its indexed
rank witness, and verifies the endpoint-capacity identity (1.2).
