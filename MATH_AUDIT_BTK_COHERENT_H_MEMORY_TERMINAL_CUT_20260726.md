# Audit and sharpening of the BTK coherent \(H\)-memory terminal cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input.

## 0. Verdict

The terminal-cut argument in
`MATH_OBSTRUCTION_BTK_COHERENT_H_MEMORY_SINK_DENSITY_20260726.md`
is valid. Its record-set bounds and its original inclusive-window
off-by-one are correct. The result is, however, much stronger than stated.
The order of the BTK active tails forces the repeated coordinate to occur
within seven edges, independently of the atom length.

### Theorem 0.1 (uniform seven-edge BTK terminal cut)

Put the fixed-order BTK symmetric-chain decomposition on both halves
\(A,B\), where \(|A|=|B|=m\), and use the standard rank-\(m\) product
diagonals as complete atoms. Let \(P\) be an atom of length \(h\ge 3\).
After either complete orientation of \(P\), every route consisting of one
Johnson seam followed by the complete adjacent endpoint atom \(Q\) contains
two uses of one physical coordinate in a window of at most seven edges.

Consequently, for every integer \(H\ge 7\), both orientations of every
complete atom of length \(h\ge3\) are sinks in the two-sided
\(H\)-memory endpoint-routing graph.

The constants by seam type are exact consequences of the proof:

| Change in the high-half word | Proved containing window |
|---|---:|
| Equal-weight internal exchange | at most 7 edges |
| One-bit cross-half change | at most 5 edges |
| Unchanged high-half word | at most 3 edges |

For a low endpoint, the same three cases are read in the \(B\)-half.

### Corollary 0.2 (exact sink census)

Let

\[
 c_m=\binom m{\lfloor m/2\rfloor}.
\]

The number of complete product atoms of length at least three is exactly

\[
 \boxed{S_m=\binom m{\lfloor (m-3)/2\rfloor}^{\!2}}
       =c_m^2-O(c_m^2/m).
\tag{0.2}
\]

In particular, if \(H=\lfloor\sqrt m\,\omega\rfloor\), where
\(\omega\to\infty\) and \(\omega=o(\sqrt m)\), then

\[
 S_m=c_m^2-o(W/H)
 =\left(\frac2{\sqrt\pi}+o(1)\right)\frac W{\sqrt m}.
\tag{0.3}
\]

Any state-valid cover made from retained complete BTK product atoms, with
one endpoint seam between consecutive atoms, which omits \(u\) middle
owners has at least

\[
                         p\ge S_m-\lfloor u/4\rfloor
\tag{0.4}
\]

components. This conclusion does not apply if atoms may be split or
internally recoded.

## 1. The audited record estimates

For a binary word \(w\), let \(R(w)\) be the set of strict ascending
record times of its prefix-height walk. If an equal-weight bit exchange
raises the walk by two on an interval, then:

* at most two record times are added inside the translated interval; and
* after the walks reunite, at most two old record times are suppressed.

No old record inside the raised interval is lost, and no new record after
the reunion is created. Therefore, in either direction,

\[
 |R(w)\setminus R(w')|\le2,
 \qquad |R(w')\setminus R(w)|\le2,
\tag{1.1}
\]

and hence \(|R(w)\triangle R(w')|\le4\). This verifies the bound used in
the original report, while retaining the stronger one-sided information.

For a one-bit change, one suffix is translated by two. In the upward
direction

\[
 R(w)\subseteq R(w'),\qquad |R(w')\setminus R(w)|\le2;
\tag{1.2}
\]

the downward direction is the reverse nesting. Thus the stated
symmetric-difference bound two is also correct.

The constants are sharp at the record-set level. For example,
\(010111\) and \(110011\) have record sets \(\{5,6\}\) and
\(\{1,2\}\), while \(01\) and \(11\) have record sets
\(\varnothing\) and \(\{1,2\}\).

## 2. Equal tails lose at most two positions

For a finite ordered set \(E\), write \(T_h(E)\) for its final \(h\)
elements.

### Lemma 2.1 (ordered-tail replacement)

Suppose

\[
 E'=(E\setminus D)\cup A,
 \qquad D\subseteq E,\qquad A\cap E=\varnothing,
\]

and both \(T_h(E)\) and \(T_h(E')\) exist. Then

\[
 |T_h(E)\setminus T_h(E')|
 \le \max\{|D|,|A|\}.
\tag{2.1}
\]

If the two tails have the same size, the reverse difference has the same
cardinality.

#### Proof

Let \(d\) of the deleted elements lie in \(T_h(E)\). After deletion, the
\(d\) vacant terminal positions are filled, when necessary, by elements
below every surviving member of \(T_h(E)\). On subsequently inserting
\(|A|\) elements, the first \(d\) possible displacements can remove only
these promoted lower elements. At most
\((|A|-d)_+\) further insertions can displace surviving members of the old
tail. Hence the number of lost old-tail elements is at most

\[
 d+(|A|-d)_+=\max(d,|A|)
 \le\max(|D|,|A|).
\]

If there are temporarily fewer than \(h\) elements, the same argument is
made after adjoining formal elements below the ordered ground set.
\(\square\)

Apply this lemma to (1.1). For an internal exchange of the \(A\)-word,
the active tails \(S,T\) have equal length \(h\), and

\[
 |S\setminus T|=|T\setminus S|\le2.
\tag{2.2}
\]

For a one-bit upward change, \(h'=h+2\), (1.2) gives

\[
                         T_h(R(w))
             \subseteq T_{h+2}(R(w')).
\tag{2.3}
\]

Indeed, above a member of \(T_h(R(w))\) there are at most \(h-1\) old
records and at most two new records. For a downward change, reversing
(2.3) gives

\[
                         T_{h-2}(R(w'))
             \subseteq T_h(R(w)).
\tag{2.4}
\]

Thus the exact active-tail profiles at adjacent high endpoints are:

\[
 \begin{array}{c|c|c|c}
 \text{seam type}&h'&|S\setminus T|&|T\setminus S|\\
 \hline
 \text{internal }A&h&\le2&\le2\\
 \text{internal }B&h&0&0\\
 \text{cross, }A\text{-rank rises}&h+2&0&2\\
 \text{cross, }A\text{-rank falls}&h-2&2&0.
 \end{array}
\tag{2.5}
\]

In particular the original overlap \(h-4\) is valid but nonsharp; the
uniform exact lower bound furnished by (2.5) is

\[
                         |S\cap T|\ge h-2.
\tag{2.6}
\]

For \(h\ge3\), a Johnson neighbor of a high endpoint has excess
\(h'\in\{h-2,h,h+2\}\), still positive, so any neighboring product-atom
endpoint is again the high endpoint of its atom. This verifies the
endpoint quantifier and improves the old threshold \(h\ge5\) to
\(h\ge3\).

## 3. The seven-edge age calculation

The BTK chain inserts its unpaired coordinates in increasing order. Let

\[
 S=\{s_1<\cdots<s_h\},
 \qquad T=\{t_1<\cdots<t_{h'}\}
\]

be the \(A\)-active tails of consecutive high-end atoms \(P,Q\).
Traversing \(P\) low-to-high uses the \(A\)-labels
\(s_1,\ldots,s_h\), while traversing \(Q\) from its high endpoint uses
\(t_{h'},\ldots,t_1\).

Put

\[
 a=|S\setminus T|,qquad b=|T\setminus S|,
\]

and choose \(c=\max(S\cap T)\). Its position \(i\) in the \(P\)-word
and its position \(\ell\) in the reversed \(Q\)-word satisfy

\[
                         i\ge h-a,
 \qquad                 \ell\le b+1.
\tag{3.1}
\]

There is exactly one seam edge between the atoms. Therefore the inclusive
number of edges from the occurrence in \(P\) through the occurrence in
\(Q\) is

\[
 q=(h+1+\ell)-i+1=h+\ell-i+2
                    \le a+b+3.
\tag{3.2}
\]

Using (2.5), this gives respectively

\[
 q\le7,qquad q\le3,qquad q\le5,qquad q\le5.
\tag{3.3}
\]

The coordinate \(c\) is inserted on the \(P\)-edge and removed on the
\(Q\)-edge, so (3.3) violates lower residence and therefore two-sided
\(H\)-safety whenever \(H\ge7\).

There is a small correction to the original prose: the seam itself cannot
use \(c\). Since \(c\in S\cap T\), it belongs to both high endpoints, so
its membership is unchanged by the seam.

For the opposite orientation, a completed high-to-low traversal of
\(P\) ends at a low endpoint. Its \(B\)-restriction is the high BTK word.
Along that traversal the \(B\)-tail is inserted increasingly; along the
successor from low to high it is removed decreasingly. Repeating
Sections 1--3 on \(B\) proves exactly the same bounds. This is a direct
proof for the second orientation.

The off-by-one is now explicit: two uses in an inclusive \(q\)-edge
subword have edge-index difference \(q-1\). The \(H\)-memory queue stores
the preceding \(H-1\) edges, so the later use is rejected precisely when
\(q\le H\). Thus \(H\ge7\), not \(H>7\), is sufficient. The original
coarse calculation \(q\le2h+3\) and condition \(2h+3\le H\) were also
off-by-one correct.

## 4. Census

If \(r=(m-h)/2\), the exact number of atoms of length \(h\) is

\[
 P_h=\binom mr^2-\binom m{r-1}^2.
\tag{4.1}
\]

Summing over the parity class of \(m\) telescopes. The atoms with
\(h\ge3\) therefore number

\[
 \sum_{\substack{h\ge3\\h\equiv m\pmod2}}P_h
 =\binom m{\lfloor(m-3)/2\rfloor}^{\!2},
\tag{4.2}
\]

which proves the exact formula in (0.2). Since the lower index differs by
only one or two from the central index,

\[
 c_m^2-S_m=O(c_m^2/m).
\tag{4.3}
\]

Also

\[
 c_m^2=\left(\frac2{\sqrt\pi}+o(1)\right)
           \frac W{\sqrt m}.
\tag{4.4}
\]

For \(H=\sqrt m\,\omega+O(1)\), the ratio of the error in (4.3) to
\(W/H\) is \(O(\omega/m)\). This proves (0.3) for the stated range and
removes the Gaussian-tail estimate needed by the weaker
\(h\le H/2+O(1)\) theorem.

Every retained sink atom must terminate its directed component. Distinct
sink atoms terminate distinct components. Because complete atoms partition
the middle owners, omitting one sink atom of length at least three omits at
least four owners. Hence a cover omitting \(u\) owners omits at most
\(\lfloor u/4\rfloor\) sink atoms. This proves (0.4).

## 5. Complement and implication scope

The low-orientation claim should not be justified by the phrase
"reverse-complement together with the half swap." The fixed-half
anti-automorphism

\[
                         \vartheta_A\times\vartheta_B
\]

does exchange high and low endpoints and could be used after tracking its
coordinate reflection. Adding the half swap preserves the high/low type
and therefore does not by itself prove the required low statement. The
clean proof is the direct \(B\)-record argument in Section 3.

Moreover, literal complementation alone does not preserve a fixed-order
BTK SCD. It sends it to the reverse-order BTK SCD. Thus this terminal cut
does not construct a literal-complement-equivariant owner-disjoint forest
inside one fixed factor. What is proved is stronger in the direction
actually needed for the obstruction: each physical orientation is a sink
by a direct record-tail argument, without any complement pairing.

The theorem rules out a long state-valid cover made from complete atoms of
the fixed BTK product factor. It does not rule out:

1. splitting an atom before the terminal record label is exposed;
2. internally recoding an atom;
3. switching to a genuinely different SCD frame at the seam; or
4. an SCD whose endpoint active tails can change in more than boundedly
   many terminal positions under a Johnson move.

No constant-one conclusion follows beyond this fixed-factor,
complete-atom obstruction.
