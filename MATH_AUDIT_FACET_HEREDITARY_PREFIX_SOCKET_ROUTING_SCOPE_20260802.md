# Audit of hereditary prefix-socket robust routing

Date: 2026-08-02  
Status: proof audit.  The multiplicative routing theorem is accepted.  Its
hereditary load hypothesis is strictly stronger than current clustered
pruning and must not be reported as proved for the reservoir bank.

## 1. Branch count

For a fixed state, successor half-sets and phase are forced.  Exactly
`h-1` entries on each shore remain freely ordered, so the raw branch count
is `(h-1)!^2`.  Revealing one permutation forward and the other backward
determines every zipper prefix/suffix resource at a unique first time.
Therefore multiplying the surviving choice counts loses no successor and
double-counts none.

## 2. Why arbitrary layer count is harmless under HPS

HPS is a min-branch condition after every surviving prefix, not an average
over paths.  Once (3.2) is at least one, a successor can be chosen greedily.
The selected successor is itself in the next kernel, where the same
hypothesis restarts.  Hence no union bound over the number of core layers
appears.

This is exactly the quantifier needed for a core path of exponential
length.

## 3. Density alone does not imply the hypothesis

Let `Omega_h` be the state set.  Its size is

\[
                         |\Omega_h|=2(2h)!,              \tag{3.1}
\]

whereas one successor neighborhood has size

\[
                         D_h=(h-1)!^2.                   \tag{3.2}
\]

For any state `omega_*`, declaring precisely `N^+(omega_*)` dead in the
next layer uses the fraction

\[
 {D_h\over|\Omega_h|}
 ={(h-1)!^2\over2(2h)!},                                \tag{3.3}
\]

which is exponentially smaller than `h^(-1/2)`, yet kills every successor
of `omega_*`.

This is not a construction killing **all** global paths; it is the exact
counterexample to deducing a hereditary statewise bound from global dead
density.  A full varying-layer no-path example is not claimed.

## 4. Factorial margin

For `rho=C/sqrt(h)`,

\[
 \log D_{\rm safe}
 \ge 2\log((h-1)!)-4C\sqrt h
 =2h\log h-O(h),                                        \tag{4.1}
\]

so the safe degree tends to infinity.  The theorem does not require a
constant surviving fraction; `exp(-O(sqrt(h)))` is adequate.

## 5. Conditional-load scope

Equation (4.1) in the theorem is exact for a target which fixes an
unordered prefix set of size `p_o`.  Several forbidden targets can kill the
same successor, so summing their weights is an upper bound, not an equality.
Endpoint resources have `p_o=0` and weight one, correctly reproducing the
common-anchor obstruction.

The present clustered-pruning theorem controls a root expectation.  It
does not control:

* every core edge;
* every oriented state;
* every surviving partial successor order;
* the residual bank after earlier reservoirs are selected.

Therefore Theorem 5.1 is a conditional implication only.  Promoting it to
an unconditional packing requires the separately stated hereditary
socket-cylinder spread theorem.

The static HPL formulation is not circular.  At one zipper shore every
variable target is a fixed old suffix union the unordered set of a new
prefix.  It becomes fully determined at one unique prefix length.  Hence
forbidden targets can be grouped into the families `mathcal F_p`, and
bounding every one-symbol link as in (2.2) directly implies the
multiplicative branch count.  Order-independent endpoint targets must be
removed before HPL is invoked; hiding them in a positive-length prefix
family would be unsound.

## 6. Verdict

The robust-routing calculation is sound and gives the right quantitative
target:

\[
 \boxed{\text{conditional fatal choice density }O(h^{-1/2})
        \Longrightarrow\text{an arbitrary-length safe path}.}
\]

The unresolved step is proving that conditional density for the actual
correlated reservoir selection.  Neither per-layer dead-half density nor
the existing average clustered-pruning estimate suffices.
