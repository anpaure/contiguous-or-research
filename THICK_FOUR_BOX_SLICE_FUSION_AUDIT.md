# Audit of thick four-box slice fusion

## 1. Verdict

The main construction and all requested leading constants are correct.
In particular:

* the nested-hook construction is a saturated symmetric-chain
  decomposition of
  \([0,h]\times[0,a]\times[0,b]\);
* its chain count is exactly

  \[
  w_3(h,a,b)
   =(h+1)(a+1)-\Psi((h+a-b)_+);
  \]

* concatenating one chain-rectangle connector per small-box chain has
  exact nonzero length

  \[
                         |P|+c\,w_3(h,a,b)-1;
  \]

* the resulting four-box bound saves exactly

  \[
                         c\,\Psi((h+a-b)_+)
  \]

  from the sorted slice construction;
* for the particular nested SCD, the full four-box width is exactly

  \[
                         \sum_j(\min(c,L_j)+1);
  \]

* the independent-connector excess is therefore exactly

  \[
                         \sum_j\max(c,L_j)-1;
  \]

* in the equal cube, the word and excess coefficients are respectively
  \(7/4\) and \(13/12\).

No source theorem is false in the nontrivial regime in which it is used.
There are two scope qualifications.

1. The local shortest-gadget argument assumes that entries assigned to a
   chain rectangle lie in that rectangle.  It is a sharp obstruction to
   the independent internal-rectangle architecture, not to words which
   use entries from several small-box chains jointly.
2. If all four side heights are zero, the quantity called excess in (1.7)
   is \(-1\), because the nonzero word deletes the unique zero whereas the
   ordinary poset width still counts it.  Every asymptotic and every
   nontrivial application has positive total height and is unaffected.

The source already states the first qualification in substance.  The
second is only a harmless degenerate convention.

## 2. The two-slice lift

Let \(W=x_1,\ldots,x_n\) cover every nonzero point of a nontrivial
join-semilattice \(P\).  The proposed word for \(P\times[0,1]\) is

\[
 (x_1,0),\ldots,(x_n,0),(0_P,1),
 (x_1,1),\ldots,(x_{n-1},1).                       \tag{2.1}
\]

It has \(2n\) entries.  A height-zero target keeps its old witness.  The
target \((0_P,1)\) is the central marker.  If \(W[i..j]\) witnesses
\(x\ne0_P\), then:

* for \(j<n\), the corresponding interval in the final copy witnesses
  \((x,1)\);
* for \(j=n\), the height-zero suffix \(W[i..n]\) followed by the marker
  witnesses \((x,1)\).

Thus

\[
                         g(P\times[0,1])\le2g(P)    \tag{2.2}
\]

is correct.  The nontriviality condition is necessary only because
\(g(\{0\})=0\) while the one-edge chain has one nonzero target.

For \(P=[0,a]\times[0,b]\times[0,c]\), the audited three-box length is

\[
                         n=(a+1)(b+c+1)-1.
\]

The bottom pair of fourth-coordinate slices costs \(2n\).  Each of the
remaining \(h-1\) positive slices costs \(n+1\), because its local zero is
a required full-box target.  Therefore

\[
 2n+(h-1)(n+1)
 =(h+1)(a+1)(b+c+1)-2,                              \tag{2.3}
\]

so the one-position improvement in Section 2 is also exact.

## 3. The chain-rectangle connector

Let

\[
 C=(c_0<\cdots<c_L),\qquad D=(d_0<\cdots<d_c).
\]

The descending-then-ascending word

\[
 (c_L,d_0),\ldots,(c_0,d_0),
 (c_0,d_1),\ldots,(c_0,d_c)                         \tag{3.1}
\]

has

\[
                         L+c+1=c+|C|               \tag{3.2}
\]

entries.  The interval beginning at \((c_i,d_0)\) and ending at
\((c_0,d_j)\) has maximum \((c_i,d_j)\).  Hence it covers the entire
rectangle \(C\times D\).

If \(C_1,\ldots,C_r\) partition \(P\), their rectangles with
\([0,c]\) partition \(P\times[0,c]\).  Concatenating the gadgets preserves
all their internal witnesses and has length

\[
 \sum_{j=1}^r(c+|C_j|)
 =cr+|P|.                                           \tag{3.3}
\]

Exactly one gadget contains the global zero.  Its unique central zero
entry may be deleted without changing any nonzero maximum, so the final
length is

\[
                         |P|+cr-1.                  \tag{3.4}
\]

This proves the connector lemma with no hidden boundary correction.

## 4. The nested-hook SCD

Let

\[
                         R=h+a+b.
\]

The standard hook decomposition of
\([0,h]\times[0,a]\), with \(h\le a\), has chains indexed by
\(0\le t\le h\).  The \(t\)-th chain starts in rank \(t\), ends in rank
\(h+a-t\), and has edge height

\[
                         q_t=h+a-2t.                \tag{4.1}
\]

It is therefore saturated and symmetric about total rank \(h+a\).

Pair this chain with \([0,b]\).  A rectangle of chain edge heights
\((q_t,b)\) has the standard hook SCD indexed by

\[
                         0\le u\le\min(q_t,b).
\]

The resulting subchain has relative edge height

\[
                         L_{t,u}=q_t+b-2u.           \tag{4.2}
\]

Its relative minimum and maximum ranks sum to \(q_t+b\).  Adding the
rank-\(t\) shift from the first hook makes the global endpoint-rank sum

\[
                         2t+q_t+b=R.                \tag{4.3}
\]

Thus every nested subchain is saturated and symmetric in the full
three-chain box.  The two hook partitions are disjoint and exhaustive, so
these subchains form an explicit SCD.

The number of subchains over the \(t\)-th first hook is

\[
                         \min(q_t,b)+1.              \tag{4.4}
\]

Consequently

\[
\begin{aligned}
 r
 &=\sum_{t=0}^h(\min(h+a-2t,b)+1)\\
 &=\sum_{t=0}^h(h+a-2t+1)
   -\sum_{t=0}^h(h+a-b-2t)_+\\
 &=(h+1)(a+1)
   -\sum_{t\ge0}(h+a-b-2t)_+.                       \tag{4.5}
\end{aligned}
\]

The replacement of the finite sum by \(t\ge0\) is legitimate because
\(d=(h+a-b)_+\le h\), using \(b\ge a\).

For \(d=2v\), the positive terms are
\(2v,2v-2,\ldots,2\), whose sum is \(v(v+1)\).  For \(d=2v+1\), they are
\(2v+1,2v-1,\ldots,1\), whose sum is \((v+1)^2\).  Hence

\[
\sum_{t\ge0}(d-2t)_+
 =\left\lceil\frac d2\right\rceil
   \left(\left\lfloor\frac d2\right\rfloor+1\right)
 =\Psi(d).                                         \tag{4.6}
\]

This proves

\[
 \boxed{
 r=(h+1)(a+1)-\Psi((h+a-b)_+).}                     \tag{4.7}
\]

Every symmetric chain contains exactly one element in the lower central
rank.  Therefore its number of chains equals the width, proving that
\(r=w_3(h,a,b)\).

As a separate finite check, direct coefficient enumeration for every
\(0\le h\le4\), \(h\le a\le5\), and \(a\le b\le6\) agrees with (4.7).
The proof above, not this check, establishes the general identity.

## 5. The \(\Psi\)-saving and Theorem A

The three-short-side volume is

\[
                         |P|=(h+1)(a+1)(b+1).
\]

Substitute (4.7) into (3.4):

\[
\begin{aligned}
 |P|+cr-1
 &=(h+1)(a+1)(b+1)\\
 &\quad+c\big((h+1)(a+1)-\Psi(d)\big)-1\\
 &=(h+1)(a+1)(b+c+1)-1-c\Psi(d).                   \tag{5.1}
\end{aligned}
\]

This is precisely Theorem A.  Since \(c>0\) whenever \(d>0\) under the
sorted nonnegative hypotheses, the saving is nonzero exactly when

\[
                         b<h+a.                     \tag{5.2}
\]

The alternative local-hook derivation is consistent.  In the
\((a,b)\)-hook indexed by \(t\), let

\[
                         q_t=a+b-2t.
\]

The old slice cost before the one global zero deletion is
\((h+1)(c+q_t+1)\).  If \(q_t<h\), the sorted three-chain constructor may
instead use

\[
                         (q_t+1)(c+h+1),
\]

and the exact difference is

\[
 (h+1)(c+q_t+1)-(q_t+1)(c+h+1)
 =c(h-q_t).                                        \tag{5.3}
\]

Writing \(t=a-r\) makes \(q_t=b-a+2r\), so the sum of the positive
deficits \(h-q_t\) is exactly \(\Psi((h+a-b)_+)\).  The \(t=0\) local
origin is the global zero and is deleted.  Each of the other \(a\) local
origins is nonzero and must be restored once.  Thus the local
interpretation has the same single final \(-1\), with no missing origin
term.

## 6. Width of the four-box and the exact excess

Let a small-box SCD chain \(C_j\) have edge height \(L_j\).  If its
minimum rank is \(s_j\), symmetry gives

\[
                         2s_j+L_j=h+a+b.            \tag{6.1}
\]

The rank polynomial of \(C_j\times[0,c]\), after removing the shift
\(s_j\), is

\[
                         (1+x+\cdots+x^{L_j})
                         (1+x+\cdots+x^c).
\]

At the lower global central rank, its relative degree is

\[
\begin{aligned}
 \left\lfloor\frac{h+a+b+c}{2}\right\rfloor-s_j
 &=\left\lfloor\frac{L_j+c}{2}\right\rfloor.        \tag{6.2}
\end{aligned}
\]

The coefficient there is the width of a two-chain rectangle:

\[
                         \min(c,L_j)+1.              \tag{6.3}
\]

The rectangles partition the full box, so their central-rank counts add.
Therefore

\[
 \boxed{
 w_4(h,a,b,c)=\sum_{j=1}^r(\min(c,L_j)+1).}          \tag{6.4}
\]

The connector length is

\[
 |P|+cr-1
 =\sum_j(c+L_j+1)-1.
\]

Subtracting (6.4) gives the exact identity

\[
\begin{aligned}
 (|P|+cr-1)-w_4
 &=\sum_j(c+L_j-\min(c,L_j))-1\\
 &=\boxed{\sum_j\max(c,L_j)-1}.                     \tag{6.5}
\end{aligned}
\]

This verifies every parity and off-by-one in Theorem B.

## 7. Scope of the architectural lower bound

For one assigned rectangle
\([0,L_j]\times[0,c]\), restrict entries to that rectangle and require its
local minimum.  For every \(1\le i\le L_j\), a witness for \((i,0)\)
contains an entry with first coordinate exactly \(i\) and second coordinate
zero.  These force \(L_j\) distinct entries.  The targets \((0,k)\),
\(1\le k\le c\), force \(c\) further entries, and \((0,0)\) forces one
more.  Thus

\[
                         L_j+c+1                   \tag{7.1}
\]

entries are necessary and the gadget (3.1) is shortest.

For the unique rectangle containing the global zero, deletion reduces the
requirement by one.  Hence (6.5) is a sharp obstruction to the declared
architecture:

* every small-box SCD chain receives its own rectangle word;
* entries of that word lie in its rectangle; and
* target witnesses remain internal to that rectangle word.

This argument is not a lower bound against arbitrary full-box words.
If entries from several SCD chains are allowed to cooperate, an entry
outside \(C_j\) but below a target in \(C_j\) may participate in its
witness.  Such cooperation is exactly cross-chain sharing, which the
source correctly identifies as the next required architecture.

Subject to this scope, the conclusion is rigorous: changing the order of
independent gadgets or choosing another SCD cannot reduce the number of
chains below the width, and no individual gadget can be shortened.

## 8. Equal-cube constants

Set \(h=a=b=c=m\).  Formula (4.7) gives

\[
\begin{aligned}
 r
 &=(m+1)^2-\Psi(m)\\
 &=\frac34m^2+O(m).                                 \tag{8.1}
\end{aligned}
\]

Consequently

\[
\begin{aligned}
 |P|+mr-1
 &=(m+1)^3+m\left(\frac34m^2+O(m)\right)-1\\
 &=\frac74m^3+O(m^2).                               \tag{8.2}
\end{aligned}
\]

The central coefficient of \((1+x+\cdots+x^m)^4\) is, by
inclusion-exclusion at degree \(2m\),

\[
\begin{aligned}
 w_4(m,m,m,m)
 &=\binom{2m+3}{3}-4\binom{m+2}{3}\\
 &=\frac23m^3+O(m^2).                               \tag{8.3}
\end{aligned}
\]

Therefore the exact-architecture excess has leading term

\[
 \left(\frac74-\frac23\right)m^3
 =\boxed{\frac{13}{12}m^3}.                         \tag{8.4}
\]

The constants \(7/4\), \(2/3\), and \(13/12\) are all correct.

## 9. Thick-sector obstruction

Put \(P_2=(h+1)(a+1)\).  Since
\(d=(h+a-b)_+\le h\),

\[
 \Psi(d)
 \le\frac{(d+1)^2}{4}
 \le\frac{(h+1)^2}{4}
 \le\frac{P_2}{4}.                                  \tag{9.1}
\]

Thus

\[
                         \frac34P_2\le r\le P_2.    \tag{9.2}
\]

Because \(c\) is the largest of the four sides,

\[
                         \frac S4\le c\le S.
\]

It follows that

\[
                         cr=\Theta(SP_2).            \tag{9.3}
\]

The exact architecture excess (6.5) is at least \(cr-1\), since every
\(\max(c,L_j)\ge c\).  It is also \(O(SP_2)\): use
\(\max(c,L_j)\le c+L_j\) and

\[
 \sum_jL_j=|P|-r\le(b+1)P_2=O(SP_2).
\]

Therefore

\[
 (|P|+cr-1)-w_4=\Theta(SP_2).                       \tag{9.4}
\]

Within this architecture, a bound

\[
                         w_4+O(S^{3-\delta})
\]

is possible exactly in the same exponent-defined thin regime

\[
                         P_2=O(S^{2-\delta}).        \tag{9.5}
\]

For equal sides \(P_2=\Theta(S^2)\), so the error remains
\(\Theta(S^3)\).  The claimed architecture obstruction is therefore
correct and is stronger when stated directly for the excess rather than
only for the total constructor length.

## 10. Degenerate convention

If \(h=a=b=c=0\), the nonzero word has length zero and the ordinary poset
width is one.  Formula (6.5) gives \(-1\), exactly reflecting that
zero-target deletion.  Calling it an excess is awkward only in this one
degenerate box.

If the total height is positive, the architecture length and the relevant
central-antichain comparison have the intended nonnegative behavior.  All
asymptotic statements and all fusion savings are in this regime.

## 11. Final theorem ledger

Certified without change:

* the trimmed bottom two-slice lift;
* the chain-rectangle connector and its single zero deletion;
* the nested three-short-side SCD;
* the exact width and \(\Psi\) formula;
* the fused four-box bound;
* the full-width decomposition over the SCD rectangles;
* the exact independent-connector excess;
* the equal-cube constants; and
* the critical-order obstruction for the independent-chain architecture.

Qualification only:

* local gadget optimality is relative to rectangle-confined entries and
  internal witnesses;
* the all-zero box has the expected width/nonzero-word convention mismatch.

Not established, consistently with the source:

* any lower bound on arbitrary four-box words from (6.5);
* a cross-chain connector with polynomial saving;
* a thick-sector \(O(S^{3-\delta})\) error; or
* the global constant-one theorem.

