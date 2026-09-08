# Gate C: exact cyclic-minimum intersections and one-ascent scarcity

**Status (2026-08-22).** Every general assertion below is proved. We give
an exact Dyck/first-return formula for the intersection of an arbitrary
coherent-tour phase with the Catalan-switched non-GK central factor. We
then prove that the natural exponential family
\(H_A=(0,A^\downarrow,(A^c)^\downarrow)\) contains only
\(2^{b+O_C(\log b)}\) phase supports with overlap at least \(q-Cb\).
This is exponentially smaller than the required
\(\Theta(4^b/b^{5/2})\) tours, so the whole one-ascent route fails.

This is not a universal obstruction to other Hamilton cycles. It
identifies an exact all-tour intersection statistic and rules out the
most economical \(2^{2b-2}\)-member near-transitive family.

Throughout,
\[
 n=2b,\qquad b\ge3\ {\rm odd},\qquad
 N=\binom{2b}{b-1},\qquad h={b-1\over2},\qquad q=b(b-1). \tag{0.1}
\]
Coordinates of binary words are read in the fixed order
\(0,1,\ldots,n-1\), and one denotes membership.

## 1. The repaired factor and its exact cyclic-minimum test

In the ordered Greene--Kleitman decomposition, greedily pair every zero
with the latest unpaired one to its left. A nonsingleton middle word \(C\)
has central flag
\[
 C-\{p_G(C)\}\subset C\subset C\cup\{q_G(C)\},           \tag{1.1}
\]
where \(p_G(C)\) is its leftmost unpaired one and \(q_G(C)\) its
rightmost unpaired zero. Thus \(q_G(C)<p_G(C)\). Balanced words with no
unpaired symbols are precisely the Dyck words.

For every primitive Dyck word \(D=1D'0\), replace the middle word
\[
                         C_D=0D'1\quad\hbox{by}\quad D.  \tag{1.2}
\]
The source has only its first zero and last one unpaired, so its arc is
\((n-1)\to0\), and \(D\) is the alternate middle of the same Boolean
diamond. Distinct sources have distinct singleton targets \(D\).
Replacing all these middles, deleting the singleton chains \(D\), and
adding singleton chains \(C_D\), therefore partitions the middle rank
again; every changed chain is still saturated and symmetric. Denote the
resulting full non-GK SCD by \(\mathscr D^*\) and its central flag factor
by \(\mathfrak F^*\).

For a middle word \(C\) and coordinate \(p\), let
\[
 R_p(C)=C_pC_{p+1}\cdots C_{n-1}C_0\cdots C_{p-1}        \tag{1.3}
\]
be its cyclic rotation. If this is Dyck, let \(\tau_p(C)\) be the
position of its first return to height zero, counted from one.

### Theorem 1.1 (exact intersection indicator)

Let \(F=(C-\{p\},C,C\cup\{q\})\) be any three-rank flag. Then
\(F\in\mathfrak F^*\) if and only if exactly one of the following holds:

\[
\begin{array}{ll}
{\rm (G)}&
q<p,\quad(p,q)\ne(n-1,0),\quad R_p(C)\ {\rm is\ Dyck},\quad
\tau_p(C)=n-p+q+1;\\[2mm]
{\rm (S)}&
(p,q)=(0,n-1),\quad C\ {\rm is\ primitive\ Dyck}.
\end{array}                                               \tag{1.4}
\]

#### Proof

In a balanced walk, an unpaired zero is exactly a down-step which reaches
a new strict prefix minimum: at that step the stack of earlier unpaired
ones is empty. Hence \(q_G(C)\), the rightmost such zero, is the first
arrival at the final global minimum. After the last visit to that
minimum, the next step is a one and can never be popped; all earlier
surviving ones would contradict that last visit. Thus this step is
\(p_G(C)\), the leftmost unpaired one.

Starting at \(p_G(C)\), the walk is Dyck, and its first return is the step
\(q_G(C)\). Conversely, suppose \(q<p\) and \(R_p(C)\) is Dyck with first
return at \(q\). Let \(a\) be the unrotated height immediately before
coordinate \(p\). On the suffix from \(p\) to \(n-1\), the rotated height
condition says that the unrotated height is at least \(a\). After the wrap,
the rotated height is \(H(i)-a\) at unrotated prefix vertex \(i\), so every
prefix height is also at least \(a\). No equality occurs before step \(q\),
and step \(q\) ends at height \(a\); hence \(q\) is the first arrival at
the global minimum. The rotation ends at the vertex immediately before
\(p\), again at height \(a\), so that vertex is the last global-minimum
visit and \(p\) is its following up-step. Thus
\(q=q_G(C),p=p_G(C)\).
Construction (1.2) removes exactly the flags with arc \((n-1)\to0\) and
adds exactly the primitive-middle flags with reversed arc
\(0\to(n-1)\). This proves (1.4). \(\square\)

### Corollary 1.2 (parity support)

Every arc of \(\mathfrak F^*\) joins opposite coordinate parities.

#### Proof

In case (G), all positions strictly between the consecutive unpaired
symbols \(q_G(C)\) and \(p_G(C)\) are paired among themselves: a pairing
cannot cross an unpaired symbol, and no unpaired symbol lies between the
rightmost unpaired zero and leftmost unpaired one. Hence
\(p-q-1\) is even and \(p-q\) is odd. Equivalently, the first-return
length \(n-p+q+1\) in (1.4) is even. The switched arc \(0\to n-1\) also
has odd difference. \(\square\)

## 2. Exact formula for every coherent phase

Let \(H=(h_0,h_1,\ldots,h_{n-1})\) be a directed Hamilton cycle, with
indices modulo \(n\), and let \(\delta\in\{0,1\}\) be its coherent phase.
Put
\[
 d_s=s(b+1),\qquad
 J_{s,t}^{\delta}=\delta+d_s+
 \bigl([t,b-1]\cup[b+1,b+t]\bigr)                         \tag{2.1}
\]
for \(0\le s<b,\ 1\le t<b\); addition in (2.1) is modulo \(n\).
Define
\[
\begin{aligned}
 r_{s,t}^{\delta}&=\delta+d_s+b+t,\\
 C_{s,t}^{\delta}(H)&=\{h_j:j\in J_{s,t}^{\delta}\},\\
 p_{s,t}^{\delta}(H)&=h_{r_{s,t}^{\delta}},\qquad
 q_{s,t}^{\delta}(H)=h_{r_{s,t}^{\delta}+1},\\
 F_{s,t}^{\delta}(H)&=
 \bigl(C_{s,t}^{\delta}-\{p_{s,t}^{\delta}\},
       C_{s,t}^{\delta},
       C_{s,t}^{\delta}\cup\{q_{s,t}^{\delta}\}\bigr).
\end{aligned}                                             \tag{2.2}
\]

### Lemma 2.1 (coherent-template formula)

The \(q\) flags in (2.2) are exactly the internal flags of the coherent
tour with projected Hamilton cycle \(H\) and phase \(\delta\).

#### Proof

Use antipodal pairs \(\{h_{\delta+j},h_{\delta+b+j}\}\). At stage zero,
after \(t\) FIFO replacements, the middle window has H-index set
\([t,b-1]\cup[b+1,b+t]\); its current and next entrants have indices
\(b+t,b+t+1\). Advancing one packet rotates the pair queue and flips all
nonspecial states, which translates every H-index by \(b+1\). Thus stage
\(s\) translates by \(d_s=s(b+1)\), proving (2.1)--(2.2).
Because \(b(b+1)\equiv0\pmod{2b}\), the \(b\) packets close. \(\square\)

Combining Theorem 1.1 and Lemma 2.1 gives the promised exact all-tour
formula:
\[
 M(H,\delta):=|\mathcal T(H,\delta)\cap\mathfrak F^*|
 =\sum_{s=0}^{b-1}\sum_{t=1}^{b-1}
 \mathbf1_{\mathfrak F^*}\!\left(F_{s,t}^{\delta}(H)\right), \tag{2.3}
\]
where every indicator is evaluated by (1.4).

For an explicit subset formula, let \(A\subseteq[1,n-1]\), put
\(B=[1,n-1]\setminus A\), and define the bijection from coordinates to
positions of \(H_A=(0,A^\downarrow,B^\downarrow)\) by
\[
\pi_A(0)=0,\quad
\pi_A(x)=
\begin{cases}
1+|\{a\in A:a>x\}|,&x\in A,\\
1+|A|+|\{y\in B:y>x\}|,&x\in B.
\end{cases}                                               \tag{2.4}
\]
Then \(x\in C_{s,t}^{\delta}(H_A)\) exactly when
\[
 \pi_A(x)-\delta-d_s\pmod n
 \in[t,b-1]\cup[b+1,b+t],                                 \tag{2.5}
\]
and \(p,q\) are the inverse images under \(\pi_A\) of the two consecutive
indices in (2.2). Equations (1.4), (2.4), and (2.5) are an exact
intersection formula in the subset \(A\).

## 3. A universal parity loss

Every edge of the projected Hamilton cycle occurs in exactly \(h\)
internal flags. Indeed, in (2.2) the arc-start index is
\(\delta+s(b+1)+b+t\). Since \(\gcd(b+1,2b)=2\), each admissible parity of
\(t\) determines a unique \(s\), and among \(1\le t<b\) each parity occurs
\(h\) times. Let
\[
 e_{\rm same}(H)=
 |\{i:h_i\equiv h_{i+1}\pmod2\}|.                         \tag{3.1}
\]
Corollary 1.2 gives
\[
 \boxed{M(H,\delta)\le q-h\,e_{\rm same}(H).}             \tag{3.2}
\]
Indeed, the \(h\) flags above a same-parity edge all fail (1.4), and the
edge classes are disjoint. Thus overlap \(q-L\) forces
\(e_{\rm same}(H)\le L/h\).

## 4. The one-ascent family has too few near-tours

Require \(n-1\in A\subseteq[1,n-1]\), and consider both phases of
\[
                         H_A=(0,A^\downarrow,B^\downarrow). \tag{4.1}
\]
If \(B\ne\varnothing\) and \(\min A<\max B\), the edge from \(\min A\)
to \(\max B\) is the
unique ascent after the initial edge \(0\to n-1\). It identifies the block
boundary, so (2.4) recovers \(A\) from the cycle; the map is injective on
these genuine one-ascent cases. If \(B=\varnothing\) or
\(\min A>\max B\), then \(A\) is a terminal interval and all such
parameters give the single descending cycle
\(H_*=(0,n-1,\ldots,1)\). Consequently the family has exactly
\[
                         2^{n-2}-(n-1)                   \tag{4.1a}
\]
genuine one-ascent cycles, plus \(H_*\). Counting parameter words instead
of distinct cycles only overcounts and is therefore valid below.

Write the membership word
\[
                         x_1x_2\cdots x_{n-1},
 \qquad x_i=\mathbf1_{\{i\in A\}},                         \tag{4.2}
\]
and let \(\omega(A)\) be the number of its odd-length runs which touch
neither endpoint of the word.

### Lemma 4.1 (odd-run obstruction)

\[
                         e_{\rm same}(H_A)\ge\omega(A).   \tag{4.3}
\]

#### Proof

An internal zero-run of length \(\ell\) is flanked by two members
\(p>q\) of \(A\) which are consecutive in \(A^\downarrow\), with
\(p-q=\ell+1\). If \(\ell\) is odd, this is a same-parity Hamilton edge.
Likewise an internal odd-length one-run gives a same-parity edge between
consecutive members of \(B^\downarrow\). Different runs give different
edges, proving (4.3). \(\square\)

It remains to count words with few odd internal runs. Put \(m=n-1\).
For run lengths, use
\[
 E(z)={z\over1-z},\qquad
 V(z)={z^2\over1-z^2},\qquad
 O(z)={z\over1-z^2},                                     \tag{4.4}
\]
for an unrestricted positive endpoint run, a positive even internal run,
and a positive odd internal run. Every nonconstant binary word has a
unique first bit and a unique composition of \(m\) into its run lengths;
conversely these data recover the word. With \(\ell\) internal runs and
exactly \(j\) odd ones, choose their \(j\) positions. Therefore words with
at most \(k\) odd internal runs have generating function bounded
coefficientwise by
\[
 2E(z)+2E(z)^2\sum_{j=0}^k
 \sum_{\ell\ge j}{\ell\choose j}V(z)^{\ell-j}O(z)^j
 =2E(z)+2E(z)^2\sum_{j=0}^k
 {O(z)^j\over(1-V(z))^{j+1}}.                            \tag{4.5}
\]
The factor two only overcounts our words ending in one.

Since
\[
                         1-V(z)={1-2z^2\over1-z^2},       \tag{4.6}
\]
the \(j\)-th nonconstant summand simplifies exactly to
\[
 2E(z)^2{O(z)^j\over(1-V(z))^{j+1}}
 ={2z^{j+2}(1-z^2)\over(1-z)^2}\,
   (1-2z^2)^{-j-1}
 ={2z^{j+2}(1+z)\over1-z}\,(1-2z^2)^{-j-1}.
\]
Expanding
\((1-2z^2)^{-j-1}=\sum_{r\ge0}\binom{r+j}{j}2^rz^{2r}\),
its coefficient of \(z^m\) is at most
\[
 4(m+1)(m+j)^j2^{m/2}.
\]
Summing \(0\le j\le k\), and adding the two constant words, gives the
fully uniform bound
\[
\#\{x\in\{0,1\}^m:\omega(x)\le k\}
\le 2+4(k+1)(m+1)(m+k)^k2^{m/2}
\le 2^{m/2}m^{O(k+1)}.                                  \tag{4.7}
\]

### Theorem 4.2 (exponential scarcity)

Let \(L=L_b\) and \(k=\lfloor L/h\rfloor\). The number of phase-labelled
supports in (4.1) satisfying \(M(H_A,\delta)\ge q-L\) is at most
\[
                         2^{b+O(1)}\,b^{O(k+1)}.          \tag{4.8}
\]
In particular, for every fixed \(C\),
\[
 \#\{(A,\delta):M(H_A,\delta)\ge q-Cb\}
 =2^{b+O_C(\log b)}.                                     \tag{4.9}
\]
The required number of tours for fixed-fraction central coverage is
\[
 {N\over q}=\Theta\!\left({4^b\over b^{5/2}}\right).      \tag{4.10}
\]
Thus (4.9) is exponentially too small even before disjointness is imposed;
even using every candidate covers only \(o(N)\) flag incidences.
The same conclusion holds for \(L=o(b^2/\log b)\).

#### Proof

Equations (3.2) and (4.3) give \(\omega(A)\le L/h=k\).
Apply (4.7) with \(m=2b-1\), and multiply by two phases, proving (4.8).
For \(L=Cb\), \(k\le3C\), giving (4.9). Comparing (4.9) with (4.10)
proves exponential insufficiency; multiplication by \(q=O(b^2)\) still
gives \(o(N)\). If \(L=o(b^2/\log b)\), then
\(k=o(b/\log b)\), so the extra factor in (4.8) is \(2^{o(b)}\), while
the leading factor is only \(2^{b+O(1)}\). \(\square\)

## 5. Exact scope

Theorem 4.2 rules out the entire two-descending-block family, despite its
\(2^{2b-2}\) raw subset parameters and its optimal-looking \(O(1)\)
number of order ascents. The obstruction is parity/run rigidity, before
any middle-target codegree or matching issue.

It does not show that all \(q-O(b)\) intersections with
\(\mathfrak F^*\) are scarce. Already the exactly parity-alternating
directed Hamilton cycles number
\[
                         b!(b-1)!:                       \tag{5.1}
\]
anchor the cycle at the even coordinate \(0\), then independently order
the \(b\) odd coordinates and the remaining \(b-1\) even coordinates.
Thus general nearly parity-alternating cycles remain factorially abundant.
The live alternatives are:

1. prove a comparable structural entropy loss from the full
   Dyck/first-return formula (2.3), obstructing the fixed
   \(\mathscr D^*\) altogether; or
2. find a large, rankwise-disjoint high-overlap subfamily across many
   Hamilton cycles and repair its \(O(b)\) defects per tour.

No fixed-fraction residual matching theorem is claimed.

## 6. Finite audit

The companion checker is
scratch/verify_gate_c_cyclic_minimum_and_one_ascent_scarcity_20260822.py.
It verifies the exact factor test, coherent template, parity support,
odd-run inequality, and finite one-ascent overlap censuses. It is
confirmatory; all general proofs are above.
