# Audit of the PBBS in-place packet primitive and erosion-provenance gate

Date: 2026-07-26

Method: independent pure-mathematics audit. No computation, finite search,
solver, or external input is used.

Audited reports:

* MATH_THEOREM_K_PBBS_INPLACE_SECTOR_CERTIFICATE_OBSTRUCTION_20260726.md;
* MATH_ATTACK_K_PBBS_INPLACE_BASELINE_REPLACEMENT_AND_CROSSING_GATE_20260726.md.

## 0. Verdict

**Pass with the scopes now written in the reports.**

The exact positive primitive is an owner-slot, packet-interior theorem:

\[
 |\mathcal Z_s|=2s+3
 \quad\text{against}\quad 2s+2
 \text{ full-packet owner occurrences}.
\tag{0.1}
\]

For \(t\) equal-height packets in \(c\) literal ordered-port chains, the
ordinary word length is

\[
 \boxed{t(2s+3)+c(s-1)}
\tag{0.2}
\]

and, only when the complete packets are owner-occurrence-disjoint, the
excess over their owner-slot baseline is

\[
 \boxed{t+c(s-1).}
\tag{0.3}
\]

The exact local obstruction is

\[
 \boxed{L_{\rm one\ parity}\ge2s+1,\qquad
        \delta\ge s-c_0-\rho.}
\tag{0.4}
\]

Thus isolated sector-local replacement has linear cost; the two-parity
circular primitive escapes by cross-parity sharing and an open ordered
port.

Neither theorem yet certifies deletion of principal endpoint-capped
\(H\)-erosion letters. The missing alignment and witness-routing statement
is precisely ERP\(_H\) in the integrated report. This is a substantive
boundary, not wording.

## 1. Local packet formulas

For the active cycle \(\Gamma=(\gamma_0,\ldots,\gamma_{2s})\), disjoint
cores \(K,K'\), and cyclic \(s\)-windows \(V_j\), the two rows

\[
 E_j=K\cup V_j,\qquad
 O_j=K'\cup W_j
\]

have the audited consecutive-target formulas

\[
 \bigcap_{j=p}^{q}E_j
 =K\cup\{\gamma_q,\ldots,\gamma_{p+s-1}\},
\]

\[
 \bigcup_{j=p}^{q}E_j
 =K\cup\{\gamma_p,\ldots,\gamma_{q+s-1}\},
\]

and

\[
\begin{aligned}
 \bigcap_{j=p}^{q}O_j
 &=K'\cup\{\gamma_0,\ldots,\gamma_{p-1}\}
       \cup\{\gamma_{s+1+q},\ldots,\gamma_{2s}\},\\
 \bigcup_{j=p}^{q}O_j
 &=K'\cup\{\gamma_0,\ldots,\gamma_{q-1}\}
       \cup\{\gamma_{s+1+p},\ldots,\gamma_{2s}\}.
\end{aligned}
\tag{1.1}
\]

The linear chart has length \(3s+2\). Its duplicated ordered port has
length \(s-1\); deleting that terminal duplicate gives the circular
length \(2s+3\). All counts and nonzero-letter conditions pass.

## 2. Port and ownership scopes

The normalized ordered port is core-blind. Swapping \(K,K'\) while
retaining the same active cycle gives literally equal normalized ports,
but the candidate seam

\[
 E_s=K\cup V_s,\qquad
 \widetilde E_0=K'\cup V_0
\]

has

\[
 E_s\cap\widetilde E_0=\varnothing,
\]

whereas a step-two rank-\(m\) Johnson edge requires intersection
\(m-1\). Hence normalized-port compatibility cannot certify physical
chronology.

Conversely, the decorated rigidity lemma is valid under its explicit
hypotheses: common carrier, exact ordered \(q-1\) active overlap, actual
successor, and shared facet equal to the carrier plus that overlap. Under
those hypotheses the token lines form one longer fixed-carrier run, so
two distinct maximal runs do not join.

The normalized type count is also correct. A length-\((s-1)\) port has
fewer than \(n^{s-2}\) types modulo rotation, and each complete phase deck
contributes at most \(n\) literal chains per type. For
\(H=O(\sqrt m)\),

\[
 2Hn^{H-1}=\exp(o(m)).
\]

This yields the claimed packet-interior little-oh ledger only after the
full-packet owner-disjointness premise is supplied.

## 3. Shallow chronology and seam constants

The centered parenthesis theorem gives

\[
 1\le\mu_2^-\le10,\qquad
 \sum(\mu_2^--1)<12B,
\]

so fewer than \(24B\) rooted lower-\(q=2\) occurrences have a nonunique
target. On the upper signed layer,

\[
 1\le\mu_2^+\le3,\qquad
 \sum(\mu_2^+-1)<4B,
\]

so the corresponding bound is \(8B\). The integrated report correctly
uses the upper statement for the complemented-row lower diagonal.

For \(J\) erased chronological boundaries, the physical signed catalogues
have sizes

\[
 2qJ\quad\text{at depth }q,
\]

\[
 6J\quad\text{through depths }1,2,
\]

and

\[
 H(H+1)J\quad\text{through depth }H.
\]

These are occurrence catalogues, not automatically repairs after deleting
erosion letters. The independent appended crossing chart has exact length
\(4H-1\) per seam; charging endpoint initialization as well gives
\(5H-1\). At \(J=\Theta(W/H)\), either established additive ledger has
order \(W\). This is not a universal lower bound on a noncellular
cross-boundary braid.

## 4. Final audited boundary

The reports prove:

* the sharp \(2s+1\) one-parity certificate obstruction;
* the \(2s+3\) two-parity circular packet primitive;
* the exact literal port-chain ledger;
* the pin-cap sharing criterion;
* the core-blind port counterexample;
* the fixed-carrier decorated rigidity lemma; and
* the exact shallow/deep crossing catalogues.

They do not prove:

* an injective alignment of credited packet owners with deleted erosion
  letters in the correct sign/parity trajectory;
* ERP\(_H\);
* full-packet cross-deck owner disjointization; or
* an \(o(W)\) \(q\ge3\) crossing braid.

Therefore the precise unresolved theorem is the conjunction of
erosion-provenance alignment and noncellular all-depth crossing fusion.
No coefficient-one implication is asserted.
