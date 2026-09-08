# Independent audit of Catalan endpoint-bank two-shadow extendability

Date: 2026-07-31  
Lane: K, recursive residual/collar interface  
Status: **GO**, with the synchronization scope stated below

## 1. Audited statement

This note audits from first principles

```text
MATH_THEOREM_CATALAN_ENDPOINT_BANK_TWO_SHADOW_EXTENDABILITY_20260731.md
SHA-256 41d0ee40060443233f65ddab87bca4abb7ee870ee975a49c1d519a6f96c11383
```

Put

\[
 X_n=\binom{[2n]}n,qquad
 K_n=\operatorname{Cat}_n=\frac1{n+1}\binom{2n}n,qquad
 P_n=\binom{2n}{n-2}.
\]

The claim is that every \(\mathcal A\subseteq X_n\) of order at most
\(K_n\) has an injective choice of contained \((n-2)\)-sets and, dually,
an injective choice of containing \((n+2)\)-sets.

## 2. Lovasz--Kruskal--Katona threshold

For \(n\ge4\),

\[
 \frac{K_n}{\binom{2n-2}{n}}
 =\frac{2(2n-1)}{(n+1)(n-1)}.
\]

This is at most one exactly when

\[
 n^2-4n+1\ge0,
\]

which holds for every integer \(n\ge4\).  Equality is not needed; at the
first case \(n=4\), the comparison is \(14<15\).

For a nonempty subfamily \(\mathcal B\subseteq\mathcal A\), write uniquely

\[
                         |\mathcal B|=\binom xn,qquad x\ge n.
\]

Monotonicity of the generalized binomial coefficient and the preceding
threshold give \(x\le2n-2\).  The Lovasz form of Kruskal--Katona, iterated
once if stated only for the immediate shadow, gives

\[
                         |\partial_2\mathcal B|ge\binom{x}{n-2}.
\]

The exact ratio is

\[
 \frac{\binom{x}{n-2}}{\binom xn}
 =\frac{n(n-1)}{(x-n+1)(x-n+2)}\ge1,
\]

because \(x-n+1\le n-1\) and \(x-n+2\le n\).  Therefore every subfamily
obeys Hall.  This proves the lower injection.  Complementation in \([2n]\)
turns a contained \((n-2)\)-set into a containing \((n+2)\)-set and proves
the upper injection.

All threshold arithmetic is exact.  No asymptotic estimate is being used.
In fact the threshold and ratio are strict for every integer \(n\ge4\), so

\[
                         |\partial_2\mathcal B|\ge|\mathcal B|+1.
\]

Consequently a bank of order at most \(K_n\) remains matchable after any
one prescribed lower-shadow target is deleted; the dual statement holds
above.  This is one-resource resilience, not positive-fraction expansion.

## 3. The exceptional base \(n=3\)

Here \(K_3=5\), and the two-step lower shadow of a triple family is its
ordinary union.  Let \(\mathcal B\) have \(t\le5\) distinct triples.  If
its union had order at most \(t-1\), all its triples would lie in a
\((t-1)\)-set.  But

\[
 \binom{t-1}{3}<t
 \qquad(1\le t\le5),
\]

with values \(0,0,0,1,4\).  This contradicts distinctness, so
\(|\partial_2\mathcal B|\ge t\), exactly Hall's condition.  The dual follows
by complementation.

The exact minimum union orders for \(t=1,\ldots,5\) are

\[
                         3,4,4,4,5.
\]

Thus Hall equality occurs for \(t=4\) and \(t=5\), and the one-resource
resilience just proved for \(n\ge4\) is false at this base.

There are

\[
                         \sum_{t=0}^{5}\binom{20}{t}=21700
\]

possible families in this base, but the displayed inequality proves all of
them simultaneously.  The exclusion of \(n=2\) is necessary: rank zero has
only the empty set, while \(K_2=2\).

## 4. Transversal-matroid rank and basis extension

Let \(T_-\) be the transversal matroid on ground set \(X_n\) induced by
containment into rank \(n-2\).  Its rank is at most \(P_n\), the size of
that target rank.  A symmetric-chain decomposition matches every
\((n-2)\)-set to the unique rank-\(n\) member of its chain.  Distinct
\((n-2)\)-sets lie on distinct chains at that rank, so this saturates the
entire target and proves

\[
                         \operatorname{rank}T_-=P_n.
\]

The upper transversal matroid has the same rank by complementation.
Theorem 1.1 says every family of order at most \(K_n\) is independent in
both matroids.  The ordinary matroid basis-extension axiom therefore extends
it to a basis of size \(P_n\).  Corollary 1.2 is valid exactly as stated.

## 5. Exact relation to Theorem 6.1

Let \(F\) be an oriented parameter-\(n\) Catalan linear matching.  It has
\(N_n\) edges on \(M_n\) middle vertices and hence \(K_n=M_n-N_n\) path
components.  Its unused-tail and unused-head banks \(E^-,E^+\) therefore
both have order \(K_n\).

Extend \(E^-\) to an upper-shadow basis \(B^-\) of order \(P_n\).  Its
complement

\[
                         S^-=X_n-B^-
\]

has order

\[
 M_n-P_n=\operatorname{Cat}_{n+1},
\]

and lies in the used-tail image of \(F\).  Pulling \(S^-\) back through the
injective tail map selects an atom set \(Q^-\) of that order.  For each
selected atom, its own tail is contained in its upper outer colour, so it
serves as the port \(p^-\); the basis matching supplies the upper diagonal
sector of Theorem 6.1.  Dually, extending \(E^+\) to a lower-shadow basis
produces a possibly different atom set \(Q^+\) and the lower diagonal
sector.

This proves exactly the following one-sided statement:

> Either diagonal sector of Theorem 6.1 can always be completed from any
> child Catalan linear forest, using a suitable deletion set on that side.

It does **not** prove \(Q^-=Q^+\).  Theorem 6.1 requires one child-atom set
\(Q\) whose tail complement is an upper-shadow basis and whose head
complement is a lower-shadow basis.  That is the common-basis/matroid-
intersection condition of Proposition 6.4.  Even after a common basis is
found, the chosen diagonal representatives and retained child edges must
form one physical linear forest.  Two-shadow extendability proves neither
common-bank synchronization nor this topology row.

## 6. Consequence for the residual theorem

The theorem strengthens only the deterministic recursive collar route.
It removes separate one-sided endpoint Hall from the hypotheses: in the
two-coordinate specialization, the incidence gate can now be stated as

\[
 \boxed{\text{one common deletion basis}\;Q
        \quad+\quad
        \text{forest-compatible representatives}.}
\]

It does not strengthen the generic logarithmic-degree residual theorem.
An arbitrary sparse partial matching need not be a Catalan linear forest,
its leave banks need not have the endpoint form above, and the theorem
does not produce matching-aligned independent-boundary absorbers or
cross-list collision dispersion.

## 7. Verdict

**GO.**  The Lovasz--Kruskal--Katona threshold, the \(n=3\) base, the
transversal-matroid basis-extension corollary, and the one-sided endpoint
interpretation are all correct.  The exact surviving gate is the common
deletion basis plus the physical linear-forest condition.  No correction to
the audited theorem is required, and no claim of integral recursive
completion or \(\nu=B\) follows.
