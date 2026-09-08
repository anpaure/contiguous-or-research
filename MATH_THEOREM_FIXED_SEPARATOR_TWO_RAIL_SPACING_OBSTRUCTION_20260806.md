# A fixed separator makes two-rail SCD charts sparse in every literal word

**Date:** 2026-08-06  
**Method:** one-coordinate suffix-window spacing  
**Status:** unconditional sharp obstruction to directly embedding the
fixed-coordinate SCD target bank at theta density.  The target bank is
exact, but a single separator coordinate supplies only \(O(L/d)\) literal
chart occurrences in a word of length \(L\).  Any theta-density use must
distribute the charts over \(\Omega(d)\) separator coordinates or replace
the fixed-separator realization.

## 1. Literal two-rail occurrences

Let

\[
                         A=(A_1,\ldots,A_L)                \tag{1.1}
\]

be a word of nonempty subsets of an \(n\)-set.  For an endpoint \(i\),
write

\[
 Z_{i,j}=A_{i-j+1}\cup\cdots\cup A_i,
 \qquad1\le j\le d.                                      \tag{1.2}
\]

Fix a coordinate \(b\).  Call adjacent endpoints \((i,i+1)\) a
**fixed-\(b\) two-rail occurrence** if there are nested sets

\[
 R_1\subset R_2\subset\cdots\subset R_{d+1}
 \subseteq[n]\setminus\{b\}                              \tag{1.3}
\]

such that

\[
 Z_{i,j}=R_{j+1},\qquad
 Z_{i+1,j}=R_j\cup\{b\}
 \qquad(1\le j\le d).                                    \tag{1.4}
\]

These are exactly the two marked rails supplied by the fixed-coordinate
SCD construction.  The definition allows an arbitrary antecedent word; it
does not assume that the preceding letters have common-core star form.

## 2. The separator-spacing theorem

### Theorem 2.1 (fixed-separator spacing)

If \((i,i+1)\) is a fixed-\(b\) two-rail occurrence, then

\[
 b\notin A_{i-d+1},\ldots,A_i,
 \qquad b\in A_{i+1}.                                    \tag{2.1}
\]

Consequently the terminal positions \(i+1\) of two distinct fixed-\(b\)
occurrences have cyclic distance at least \(d+1\).

In a cyclic word of length \(L\), the number \(H_b\) of such occurrences
satisfies

\[
                         \boxed{H_b\le\left\lfloor{L\over d+1}\right\rfloor.}
                                                                    \tag{2.2}
\]

In a union of \(c\) linear regions of total length \(L\),

\[
                         H_b\le {L\over d+1}+c.             \tag{2.3}
\]

#### Proof

The depth-\(d\) value at the first endpoint is

\[
 A_{i-d+1}\cup\cdots\cup A_i=R_{d+1},                    \tag{2.4}
\]

which omits \(b\).  Hence every one of its constituent letters omits
\(b\).  The depth-one value at the second endpoint is

\[
                         A_{i+1}=R_1\cup\{b\},              \tag{2.5}
\]

so it contains \(b\).  This proves (2.1).

If two terminal positions \(e<e'\) had cyclic distance at most \(d\),
then \(A_e\) would contain \(b\) by the first occurrence, but would be
one of the \(d\) preceding \(b\)-free letters required by the second.
This is impossible.  Packing points at mutual cyclic distance at least
\(d+1\) proves (2.2).  Cut each linear region to a cycle after allowing
one boundary exception; summing gives (2.3). \(\square\)

### Remark 2.2 (the orientation is forced)

The two rails cannot simply be reversed in time.  If the \(b\)-containing
rail were immediately followed by the \(b\)-free rail, then the latter's
depth-two suffix would contain the former's depth-one letter and hence
would contain \(b\), contradicting (1.4).  Thus orientation reversal does
not double the literal density.

## 3. Theta-reset consequence

For the top merged-PBBS slab, let

\[
                         L=B(k)+O(1)=W+O(d)                \tag{3.1}
\]

be the final physical length, where \(d=\Theta(\sqrt k)\) and

\[
 \eta=2\sigma-1
     =4\sum_{r\ge1}e^{-4\pi r^2}>0.                       \tag{3.2}
\]

The reset ledger requires

\[
                         H=(\eta+o(1))W                    \tag{3.3}
\]

shared joins: one two-endpoint packet saves one otherwise private reset.

### Corollary 3.1 (one fixed SCD shore cannot pay theta)

All charts from one fixed-\(b\) SCD bank contribute at most

\[
                         {W+O(d)\over d+1}=o(W)             \tag{3.4}
\]

literal shared joins.  Hence, despite its
\((e^{-\pi}+o(1))W\) pairwise target-disjoint marked-endpoint capacity,
that bank alone cannot supply (3.3).

This conclusion is unaffected by assigning other PBBS pieces to the
intervening positions: Theorem 2.1 is a spacing constraint on the chart
terminal events themselves, not a claim that the intervening positions
must be empty.

### Corollary 3.2 (a growing separator bank is necessary)

Suppose every chosen two-rail chart is of form (1.4), with its separator
drawn from a set \(D\) of \(t\) coordinates.  Then

\[
 H\le t\left({L\over d+1}+c\right)                         \tag{3.5}
\]

on \(c=O(1)\) regions.  If (3.3) holds, then

\[
                         \boxed{t\ge(\eta-o(1))d.}          \tag{3.6}
\]

Thus no bounded tag/separator bank can turn the fixed-coordinate target
packing into the required physical reset bank.

#### Proof

Assign every occurrence to its separator and sum (2.3) over the \(t\)
coordinates.  Since \(L/W\to1\), equation (3.3) implies (3.6).
\(\square\)

## 4. Exact warm-up interpretation

The local common-core realization of one chart is

\[
 Q\cup\{a_d\},Q\cup\{a_{d-1}\},\ldots,
 Q\cup\{a_1\},Q\cup\{b\}.                               \tag{4.1}
\]

The first \(d-1\) positions are often called its warm-up.  It would be
too strong to conclude that they must be unused: a global construction may
assign other targets to them.  What Theorem 2.1 proves exactly is the
relevant nonoverlap statement:

> no second chart using the same separator \(b\) can terminate anywhere
> in those \(d\) positions.

Therefore the warm-up cannot be amortized by concatenating or densely
overlapping charts inside the single fixed-\(b\) SCD bank.  To amortize it
at theta density one needs charts with many different separators, and
their marked targets must be selected jointly across those shores.

## 5. The corrected next theorem

The all-depth target-disjointness problem for one fixed separator is solved,
but it is not the physical PBBS theorem.  The next sufficient statement is:

> **Multiseparator BTK chart theorem.**  Select
> \((\eta+o(1))W\) recursive-SCD two-rail occurrences whose separators use
> at least \(\Omega(d)\) coordinates, whose marked target rails are jointly
> disjoint across different separator shores, and whose insertion events
> occur in one PBBS-compatible owner/Euler chronology.

The fixed-coordinate SCD theorem handles disjointness *within* one shore;
Theorem 2.1 proves why a cross-shore construction is unavoidable.

## 6. Scope

Proved here:

* an exact literal spacing law independent of the chosen antecedent;
* an \(O(L/d)\) upper bound for one fixed separator;
* impossibility of paying the theta reset from one fixed-\(b\) SCD bank;
* necessity of \(\Omega(d)\) separator coordinates for this packet form.

Not proved here:

* impossibility of a multiseparator construction;
* cross-separator target disjointness;
* PBBS owner-envelope or Euler placement; or
* \(\nu(k)\le B(k)+O(1)\).

The result is therefore a sharp scope correction, not a no-go for the
two-endpoint architecture itself.
