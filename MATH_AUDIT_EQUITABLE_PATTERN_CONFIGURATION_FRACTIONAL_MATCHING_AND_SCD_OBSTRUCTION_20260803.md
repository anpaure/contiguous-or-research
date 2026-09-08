# Audit: equitable-pattern configuration law and saturated-prechain obstruction

**Date:** 2026-08-03  
**Audited file:**
MATH_THEOREM_EQUITABLE_PATTERN_CONFIGURATION_FRACTIONAL_MATCHING_20260803.md  
**Method:** independent symbolic and line-by-line audit. No finite search or
solver is used.

## 0. Verdict

**GO at exactly the stated scopes.**

The uniform configuration weights form a fractional matching saturating all
pattern and owner vertices, with target load

\[
                         \frac{N_s}{\binom{2r}{s}}\le1.
\]

The complete pair ledger is correct on the supported retained residual
band. The adaptive-boundary equivalence is exact. The saturated-prechain
deficiency formula is the Hall deficiency of a nested threshold graph, and
the consecutive-rank corollary gives a genuine \(\Omega(W)\) obstruction
for residual pairs \(O(\sqrt r)\) below the middle.

None of these results supplies an integral unrestricted configuration
matching, a Ferrers boundary, or a literal chronology.

The earlier file
MATH_THEOREM_NONCONTIGUOUS_COLLAR_EXACT_RANK_MULTIPLICITY_DECOMPOSITION_20260803.md
was a special-case draft of the now-authoritative equitable rank-law
theorem and has been retired. Its edge-colouring argument is subsumed by
MATH_THEOREM_NONCONTIGUOUS_RANK_LAW_EQUITABLE_INTEGER_DECOMPOSITION_20260803.md;
the audit below starts from that authoritative schedule.

## 1. Uniform fractional configuration audit

For one pattern \(i\), there are \(Wr!\) labelled configurations, so weight
\(1/(Wr!)\) gives degree one. For one owner \(T\), there are \(W\) pattern
choices and \(r!\) orders, again giving degree one.

Fix \(S\in\binom{[2r]}s\). For one pattern containing rank \(s\), the
number of owner-order pairs with prefix \(S\) is

\[
 \binom{2r-s}{r-s}s!(r-s)!.
\]

After multiplying by \(1/(Wr!)\), this is

\[
 \frac{\binom{2r-s}{r-s}}{W\binom rs}
 =\frac1{\binom{2r}s}.
\]

Summing over the \(N_s\) active patterns gives the asserted target degree.
The hypothesis \(N_s\le\binom{2r}s\) is exactly target capacity one. Every
edge has one pattern vertex, so the total fractional edge weight is \(W\).

## 2. Pair-ledger audit

For a fixed pattern-owner pair, summing the \(r!\) orders gives \(1/W\).
For an active pattern-rank-\(s\) target pair, the same prefix count gives
\(1/\binom{2r}s\), whose ratio to the target degree is \(1/N_s\).

For \(S\subseteq T\), fixed owner \(T\), the \(N_s\) active patterns and
\(s!(r-s)!\) compatible orders give

\[
 d_x(o_T,S)=\frac{N_s}{W\binom rs}.
\]

Dividing by \(d_x(S)=N_s/\binom{2r}s\) gives

\[
 \frac{\binom{2r}s}{W\binom rs}
 =\frac1{\binom{2r-s}{r-s}}.
\]

For a flag \(S\subset U\) of ranks \(s<t\), one active pattern contributes
\[
 \frac1{\binom{2r}t\binom ts},
\]
so summing the \(N_{s,t}\) joint patterns gives the theorem's formula.
Normalizing by either endpoint gives

\[
 \frac{N_{s,t}}{N_t\binom ts},
 \qquad
 \frac{N_{s,t}}{N_s\binom{2r-s}{t-s}}.
\]

Both are bounded by the corresponding reciprocal binomial coefficient.
Residual nonadjacency gives \(t-s\ge2\); on
\(s,t=r-o(r)\), both denominators are \(\Omega(r^2)\). Owner-target pairs
have \(r-s\ge2\) on the retained band and obey the same scale. Pattern and
owner pairs give the separate \(1/W\) term, and pattern-target pairs give
the \(1/N_s\) term. This exhausts all vertex-type pairs and verifies the
normalized ledger.

The conclusion \(K^2\rho_2=O(r^{-1})\) additionally uses
\(K\le d+2=O(\sqrt r)\) and exponentially large positive \(N_s\). Those
hypotheses are stated.

## 3. Adaptive-boundary equivalence audit

A size-\(W\) matching contains every pattern exactly once because there
are \(W\) pattern vertices, and every owner exactly once because there are
\(W\) owner vertices. Rank \(s\) occurs in \(N_s\) selected configurations.
Hypergraph disjointness makes their \(N_s\) target vertices distinct. The
unselected rank-\(s\) targets therefore form a boundary of size
\(\binom{2r}s-N_s\).

Conversely, any exact flag assignment outside boundary families of those
sizes gives \(W\) configurations with disjoint pattern, owner, and target
vertices. Thus the equivalence is exact. It does not impose the later
Ferrers geometry on the omitted targets, and the theorem explicitly says
so.

## 4. Saturated-prechain Hall audit

In any partition of the lower half into \(W\) saturated chains ending at
the rank-\(r\) owners, a chain of minimum rank \(h\) contains a rank-\(t\)
member if and only if \(h\le t\). Since the chains partition the
rank-\(t\) layer,

\[
 \#\{C:h(C)\le t\}=\binom{2r}t.
\]

A nonempty pattern \(R_i\) is compatible with \(C\) exactly when
\(h(C)\le\min R_i\). These are nested threshold neighbourhoods. The
patterns with deadline at most \(t\) have Hall deficiency

\[
 A(t)-\binom{2r}t.
\]

For any other nonempty pattern family \(X\), taking
\(t=\max_{i\in X}\min R_i\) gives
\(|X|\le A(t)\) and the same threshold neighbourhood. A family containing
an empty pattern sees all \(W\) chains and has no positive deficiency.
Hence the maximum Hall deficiency is precisely

\[
 \max_t\left(A(t)-\binom{2r}t\right)_+.
\]

The deficiency form of Hall's theorem therefore gives maximum matching
size \(W-\delta_{\rm sat}\). A perfect threshold matching selects
disjoint saturated chains, so the named targets are automatically distinct
and nested.

## 5. Consecutive-rank obstruction audit

If ranks \(s,s+1\) cannot coexist in one pattern, their active pattern sets
are disjoint. All \(N_s+N_{s+1}\) such patterns have deadline at most
\(s+1\), so

\[
 \delta_{\rm sat}\ge
 N_s+N_{s+1}-\binom{2r}{s+1}.
\]

For \(N_j=\binom{2r}j-b_j\), cancellation leaves

\[
 \binom{2r}s-b_s-b_{s+1}.
\]

At distance \(O(\sqrt r)\) from the middle,
\(\binom{2r}s=\Theta(W)\), while the whole triangular boundary has only
\(O(d^2)=O(r)=o(W)\) targets. The lower bound is therefore
\(\Omega(W)\).

This obstruction applies only to a frozen saturated prechainization such
as one SCD. Skip chains or correlated cross-chain splices are not covered,
so the theorem does not overclaim a no-go for the unrestricted
configuration hypergraph.

## 6. Proof-safe endpoint

The verified chain of implications is

\[
\boxed{
\begin{array}{c}
\text{exact equitable rank patterns}\\
\Downarrow\\
\text{canonical feasible fractional configuration matching}\\
\Downarrow\ \text{(integrality open)}\\
\text{named owner flags with adaptive boundary}.
\end{array}}
\]

The single-SCD route across the open implication has linear deficiency.
The surviving target is therefore an unrestricted Boolean skip-chain
rounding or an integral collar absorber with \(\Theta(W)\) correlated
cross-chain splices.
