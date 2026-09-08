# PBBS proximity via an (n)-spaced cut lattice

Date: 2026-07-27

## 1. Setup

Let

\[
 n=2m+1,qquad W=\binom{n}{m},qquad B=W/n=\operatorname{Cat}_m.
\]

For an oriented PBBS component (C), write

\[
 g_0,g_1,\ldots,g_{L-1}
\]

for its cyclic omitted-coordinate word.  Point balance implies
(L=\ell n) and that every coordinate occurs exactly (ell) times.
The sum of the levels (ell) over all PBBS components is (B).

Recall that (kappa(F_{m PBBS})) is the minimum number of PBBS edges
which must be deleted so that every residual path has pairwise distinct
omitted labels.  It is a lower bound on the distance to every wreath factor.

## 2. One fixed block

Fix a prospective cut position (s).  Delete the positions (s) and
(s+n), and consider the strict interior label word

\[
 g_{s+1},\ldots,g_{s+n-1}.
\]

Scan it from left to right.  Whenever the current label has already occurred
since the last deletion, delete the current position and reset the set of
seen labels.  Let (e_C(s)) be the number of additional deletions.

### Lemma 2.1

The greedy rule uses the minimum possible number of additional deletions
inside this block, subject to its two boundary cuts.

#### Proof

For every pair of consecutive equal labels in the current linear piece,
form the closed interval between their positions.  A deletion set leaves
only label-simple runs exactly when it meets every such interval.  The
greedy rule chooses the right endpoint of the interval with earliest right
endpoint.  This is the standard optimal interval-stabbing algorithm.  After
that endpoint is removed, resetting the seen-label set is precisely the
residual line instance. (square)

## 3. Averaging the lattice offset

For (a\in\{0,\ldots,n-1\}), impose the (n)-spaced cut lattice

\[
 D_a=\{a,a+n,\ldots,a+(\ell-1)n\}\pmod L.
\]

Its (ell) blocks are repaired independently by Lemma 2.1, so it gives a
valid cut set of size

\[
 \ell+\sum_{j=0}^{\ell-1}e_C(a+jn).
\]

Averaging over (a) yields

\[
 \min_a|D_a^{\rm repaired}|
 \le
 \ell+\frac1n\sum_{s=0}^{L-1}e_C(s).                 \tag{3.1}
\]

The cyclic-coordinate action is free on middle sets and commutes with PBBS.
After quotienting physical transition edges by rotation, the (W) starts
become the (B) normalized Dyck roots (mathcal D_m).  Label equality—and
hence (e_C(s))—is invariant under the spatial phase.  Write (e_m(D)) for
the common value above the root (D).

Summing (3.1) over components proves the main reduction.

### Theorem 3.1 (unit-window lattice bound)

\[
 \boxed{
 \kappa(F_{\rm PBBS})
 \le B+\sum_{D\in\mathcal D_m}e_m(D).}              \tag{3.2}
\]

An existing label-simple (n)-cycle may be left cyclic with zero cuts, so
(3.2) can only overcharge those components.

### Corollary 3.2

The single Catalan-average estimate

\[
 \boxed{
 \sum_{D\in\mathcal D_m}e_m(D)=O(B)}               \tag{UWR}
\]

implies

\[
 \kappa(F_{\rm PBBS})=O(B).
\]

Thus (UWR) is a sufficient, one-window form of the Catalan PBBS proximity
theorem.  It does not choose wreath endpoints; sewing the resulting paths
remains a strictly stronger gate.

## 4. Exact quotient formula

For a normalized Dyck root (D_0=D), let

\[
 D_{t+1}=\phi(D_t),qquad
 \lambda_0=0,qquad
 \lambda_{t+1}=\lambda_t+\delta(D_t)\pmod n.
\]

Then (e_m(D)) is obtained by applying the greedy first-repeat deletion rule
to

\[
 \lambda_1,\lambda_2,\ldots,\lambda_{n-1}.          \tag{4.1}
\]

This makes (UWR) a finite Catalan sum involving only the exact first-maximum
map; no physical factor or random occupancy model remains.

The height-gap theorem gives only

\[
 e_m(D)\le\frac{n}{2\operatorname{ht}(D)+1}.
\]

After summing over Dyck roots this is (O(B\sqrt m)), the already-known
critical estimate.  Proving (UWR) therefore still requires the missing
factor (sqrt m); the lattice reduction has localized it but not paid it.

## 5. Exact finite values

`scratch/audit_pbbs_unit_window_lattice.py` gives

\[
\begin{array}{c|rrrrrrrrrr}
m&3&4&5&6&7&8&9&10&11&12\\ \hline
B^{-1}\sum_De_m(D)
&.400&.714&.881&.985&1.014&1.020&1.066&1.140&1.197&1.234.
\end{array}
\]

The corresponding certified upper bound in (3.2) ranges from (1.40B) to
(2.234B).  Optimizing the lattice offset independently on each physical
component is slightly better; for (m=3,\ldots,10) it costs

\[
1.00,1.50,1.81,1.95,1.99,2.02,2.06,2.09
\]

cuts per Catalan packet (already-wreath components retained for free).

These computations are consistent with (UWR), but they are not evidence of
a uniform asymptotic bound by themselves.  The mean is still increasing in
the audited range.

## 6. Search consequence

The certificate generator
`n_spaced_lattice_cut_certificate` in
`scratch/pbbs_wreath_search_metrics.py` now supplies an explicit
near-(2B) starting fragmentation instead of an arbitrary optimizer of the
return-arc hitting problem.  Its fragments remain physical PBBS paths and
can be passed directly to the endpoint-sewing search.

The exact remaining order is:

1. prove (UWR), or find its asymptotic failure;
2. choose offsets/cuts jointly with endpoint-compatible path sewing;
3. impose the signed annular (o(W)) objective on the resulting exact owner
   cover; and
4. realize it by merge--reorder--split switches.

