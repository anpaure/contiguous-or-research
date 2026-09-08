# Global component effect of the \(k=11\) fork portal: exact residual phase gate

Date: 2026-07-27

Method: action-profile and port-pairing reduction; no computational search.

## 0. Outcome

The explicit three-alpha fork certainly destroys the isolation of the
alternating component, but the exact change in the total number of the
twelve PBBS components is not determined by the endpoint tables alone.

It reduces to one finite phase object:

> the component membership and cyclic order of six explicitly listed PBBS
> chords, equivalently the outside-path involution on twelve ports.

No further load, marginal, or alpha-availability condition remains. Once
this involution is known, the exact component count after the portal is the
cycle count of a fixed product of two involutions.

## 1. The net \(7\leftrightarrow7\) trade

Use the notation of
K11_PBBS_EXPLICIT_THREE_ALPHA_FORK_PORTAL_20260727.md. Relative to the
initial PBBS factor, the seven deleted chords are

\[
\begin{array}{c|c}
\text{lower row}&\text{deleted pair}\\ \hline
Z=\{1,3,5,7,9\}&\{0,10\}\\
B_1=\{1,5,7,9,10\}&\{4,2\}\\
B_2=\{2,5,7,9,10\}&\{4,0\}\\
B_3=\{0,5,7,9,10\}&\{4,1\}\\
C_1=\{1,4,5,7,9\}&\{3,10\}\\
C_2=\{4,5,7,9,10\}&\{3,0\}\\
C_3=\{0,4,5,7,9\}&\{3,1\}.
\end{array}
\tag{1.1}
\]

The seven final inserted chords are

\[
\begin{array}{c|c}
\text{lower row}&\text{inserted pair}\\ \hline
Z&\{0,4\}\\
B_1&\{0,3\}\\
B_2&\{4,1\}\\
B_3&\{4,2\}\\
C_1&\{0,10\}\\
C_2&\{3,1\}\\
C_3&\{3,10\}.
\end{array}
\tag{1.2}
\]

Tables (1.1)--(1.2) are the complete net topology; the two temporary supply
diamonds have cancelled.

## 2. Fourteen-port permutation formula

Delete the seven edges in (1.1). Every affected original PBBS component
breaks into paths. Let

\[
\tau
\]

be the fixed-point-free involution pairing the two endpoint ports of each
such residual path. Let

\[
\rho
\]

be the fixed-point-free involution pairing ports according to the seven new
edges in (1.2).

Then the affected components of the final factor are exactly the alternating
cycles of the two-coloured graph \(\tau\cup\rho\), equivalently the cycles of
\(\tau\rho\) with the standard factor-two convention. Thus the exact
component derivative is a cycle-count calculation once \(\tau\) is known.

For the alternating deleted edge, write

\[
a=Z+0,\qquad b=Z+10.
\]

It is the only deleted edge on the initial alternating component, so

\[
\tau(a)=b.
\tag{2.1}
\]

The inserted matching satisfies

\[
\rho(a)=C_1+3,\qquad
\rho(b)=B_1+0,
\tag{2.2}
\]

which are outside ports. Equations (2.1)--(2.2) prove the local portal
statement: the \(\tau\cup\rho\) cycle containing the alternating residual
path also contains outside strands.

The total component count depends only on the restriction

\[
\tau_{\rm out}
\]

to the twelve ports belonging to \(B_1,B_2,B_3,C_1,C_2,C_3\).

## 3. Why only two binary phase questions appear initially

Delete the common forward survivor and rotate each lower row to its Dyck
word. For the first supply alpha:

\[
\begin{array}{c|c|c}
\text{row}&\text{Dyck word}&\operatorname{pk}\\ \hline
B_1&1010110100&4\\
B_2&1010110010&4\\
B_3&1010111000&3.
\end{array}
\tag{3.1}
\]

For the second:

\[
\begin{array}{c|c|c}
\text{row}&\text{Dyck word}&\operatorname{pk}\\ \hline
C_1&1101010010&4\\
C_2&1101011000&3\\
C_3&1101010100&4.
\end{array}
\tag{3.2}
\]

The action profile is constant on a physical PBBS component. Therefore

- \(B_3\) is on a different component from \(B_1,B_2\);
- \(C_2\) is on a different component from \(C_1,C_3\).

The only same-profile membership questions inside the two initial alpha
charts are

\[
B_1\stackrel{?}{\sim}B_2,
\qquad
C_1\stackrel{?}{\sim}C_3.
\tag{3.3}
\]

If a pair in (3.3) is on distinct components, that alpha is a ternary
connector and merges three cycles. If it is on one component, the alpha is
a binary candidate and its effect is decided by the cyclic interlacement of
the two cuts:

- favourable order: it absorbs the third component;
- unfavourable order: it reconnects to two components without decreasing
  their number.

After the first switch, the second question must be interpreted in the
spliced factor, so the two bits are coupled. This coupling is precisely the
outside-path involution \(\tau_{\rm out}\).

## 4. Exact smallest residual obstruction

To determine the full component effect without search, it suffices to prove
the following finite phase lemma.

### Phase lemma

Determine, in the original \(f^{-2}\)-cycles:

1. whether \(B_1,B_2\) lie on the same physical cycle and, if so, their
   retained-path order;
2. whether \(C_1,C_3\) lie on the same physical cycle and, if so, their
   retained-path order;
3. which of the \(B\)- and \(C\)-rows share a physical component;
4. the induced pairing of their twelve ports after all six edges are cut.

These four items determine \(\tau_{\rm out}\), hence the exact effect of the
fork on all twelve PBBS components.

This is strictly smaller than another alpha-supply problem. All six chords
are explicit, every switch is already known to be executable, and the final
reconnection \(\rho\) is fixed by (1.2). The missing theorem is only a
phase-resolved statement about six positions on the canonical PBBS cycles.

## 5. Consequence for subsequent absorption

The existing pure-alpha atlas can Hamiltonize the post-portal factor only
after the phase lemma is supplied, because:

- component labels can migrate under the fork;
- a chart that was ternary initially may become a three-cut chart on one
  already merged cycle;
- a binary chart is useful only in the favourable retained-path order.

Thus chart abundance alone still does not prove a spanning absorption
sequence. The exact next gate is the six-chord phase lemma, not another
count of alpha charts.

## 6. Equivariant variant

The eleven translated net trades are support-disjoint because the seven
rows in (1.1) lie in seven distinct translation orbits. Hence the
equivariant orbit move is well-defined.

Its quotient component effect is again a permutation problem: replace the
fourteen labelled ports by their seven quotient edges and include the
translation voltage on each residual path. The orbit move merges to one
lifted cycle only if the resulting quotient cycle has nonzero total voltage.
The labelled phase lemma and the quotient voltage lemma are related but not
identical.
